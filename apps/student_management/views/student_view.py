from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.student_management.services.student_service import get_students
from apps.student_management.models.student_model import Student, Course
from apps.student_management.serializers.student_serializer import StudentSerializer


# CREATE
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# GET ALL (pagination + filter)
@api_view(['GET'])
def get_students_api(request):
    name = request.GET.get('name')
    page = int(request.GET.get('page', 1))
    size = int(request.GET.get('size', 5))

    students = get_students(name)

    total = students.count()

    start = (page - 1) * size
    end = start + size

    serializer = StudentSerializer(students[start:end], many=True)

    return Response({
        "total": total,
        "page": page,
        "size": size,
        "data": serializer.data
    })


# GET BY ID
@api_view(['GET'])
def get_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        return Response(StudentSerializer(student).data)
    except Student.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


# UPDATE
@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({"message": "Deleted"})
    except Student.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


# ENROLL STUDENT TO COURSE
@api_view(['POST'])
def enroll_student_to_course(request, student_id, course_id):
    try:
        student = Student.objects.get(pk=student_id)
        course = Course.objects.get(pk=course_id)
        student.courses.add(course)
        return Response({"message": "Enrolled"})
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)


# UNENROLL STUDENT FROM COURSE
@api_view(['DELETE'])
def unenroll_student_from_course(request, student_id, course_id):
    try:
        student = Student.objects.get(pk=student_id)
        course = Course.objects.get(pk=course_id)
        student.courses.remove(course)
        return Response({"message": "Unenrolled"})
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)
