from django.urls import path
from apps.student_management.views.student_view import *

urlpatterns = [
    path('students/', get_students_api),
    path('students/<int:pk>/', get_student),
    path('students/create/', create_student),
    path('students/update/<int:pk>/', update_student),
    path('students/delete/<int:pk>/', delete_student),
    path('students/<int:student_id>/enroll/<int:course_id>/', enroll_student_to_course),
    path('students/<int:student_id>/unenroll/<int:course_id>/', unenroll_student_from_course),
]