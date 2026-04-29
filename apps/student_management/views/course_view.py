from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.student_management.models.student_model import Course
from apps.student_management.serializers.course_serializer import CourseSerializer


# CREATE
@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# GET ALL
@api_view(['GET'])
def get_courses_api(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


# GET BY ID
@api_view(['GET'])
def get_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        return Response(CourseSerializer(course).data)
    except Course.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


# UPDATE
@api_view(['PUT'])
def update_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
def delete_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({"message": "Deleted"})
    except Course.DoesNotExist:
        return Response({"error": "Not found"}, status=404)
