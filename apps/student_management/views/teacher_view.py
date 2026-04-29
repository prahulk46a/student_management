from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.student_management.models.student_model import Teacher, Subject, Student
from apps.student_management.serializers.teacher_serializer import TeacherSerializer


# CREATE
@api_view(['POST'])
def create_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# GET ALL
@api_view(['GET'])
def get_teachers_api(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


# GET BY ID
@api_view(['GET'])
def get_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
        return Response(TeacherSerializer(teacher).data)
    except Teacher.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


# UPDATE
@api_view(['PUT'])
def update_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = TeacherSerializer(teacher, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
def delete_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response({"message": "Deleted"})
    except Teacher.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


# ASSIGN SUBJECT TO TEACHER
@api_view(['POST'])
def assign_subject_to_teacher(request, teacher_id, subject_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        subject = Subject.objects.get(pk=subject_id)
        teacher.subjects.add(subject)
        return Response({"message": "Assigned"})
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found"}, status=404)
    except Subject.DoesNotExist:
        return Response({"error": "Subject not found"}, status=404)


# REMOVE SUBJECT FROM TEACHER
@api_view(['DELETE'])
def remove_subject_from_teacher(request, teacher_id, subject_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        subject = Subject.objects.get(pk=subject_id)
        teacher.subjects.remove(subject)
        return Response({"message": "Removed"})
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found"}, status=404)
    except Subject.DoesNotExist:
        return Response({"error": "Subject not found"}, status=404)


# ASSIGN STUDENT TO TEACHER
@api_view(['POST'])
def assign_student_to_teacher(request, teacher_id, student_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        student = Student.objects.get(pk=student_id)
        teacher.students.add(student)
        return Response({"message": "Assigned"})
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found"}, status=404)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)


# REMOVE STUDENT FROM TEACHER
@api_view(['DELETE'])
def remove_student_from_teacher(request, teacher_id, student_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        student = Student.objects.get(pk=student_id)
        teacher.students.remove(student)
        return Response({"message": "Removed"})
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found"}, status=404)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)
