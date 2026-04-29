from rest_framework import serializers
from apps.student_management.models.student_model import Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    courses_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), many=True, write_only=True, source='courses'
    )

    class Meta:
        model = Student
        fields = '__all__'