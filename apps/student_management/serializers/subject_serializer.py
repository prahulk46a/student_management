from rest_framework import serializers
from apps.student_management.models.student_model import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
