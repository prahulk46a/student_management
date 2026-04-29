from rest_framework import serializers
from apps.student_management.models.student_model import Course, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    subjects_ids = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), many=True, write_only=True, source='subjects'
    )

    class Meta:
        model = Course
        fields = '__all__'
