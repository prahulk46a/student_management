from rest_framework import serializers
from apps.student_management.models.student_model import Teacher, Subject, Student

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    subjects_ids = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), many=True, write_only=True, source='subjects'
    )
    students = StudentSerializer(many=True, read_only=True)
    students_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), many=True, write_only=True, source='students'
    )

    class Meta:
        model = Teacher
        fields = '__all__'
