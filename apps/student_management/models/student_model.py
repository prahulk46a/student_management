from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    subjects = models.ManyToManyField(Subject, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    students = models.ManyToManyField('Student', related_name='teachers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
