from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.student_management.models.student_model import Subject
from apps.student_management.serializers.subject_serializer import SubjectSerializer


# CREATE
@api_view(['POST'])
def create_subject(request):
    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# GET ALL
@api_view(['GET'])
def get_subjects_api(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


# GET BY ID
@api_view(['GET'])
def get_subject(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
        return Response(SubjectSerializer(subject).data)
    except Subject.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


# UPDATE
@api_view(['PUT'])
def update_subject(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = SubjectSerializer(subject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
def delete_subject(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return Response({"message": "Deleted"})
    except Subject.DoesNotExist:
        return Response({"error": "Not found"}, status=404)
