from django.contrib import admin
from .models.student_model import Student, Subject, Course, Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Teacher)
