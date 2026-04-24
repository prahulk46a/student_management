from apps.student_management.models.student_model import Student

def get_students(name=None):
    qs = Student.objects.all().order_by('id')

    if name:
        qs = qs.filter(name__icontains=name)

    return qs