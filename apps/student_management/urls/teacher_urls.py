from django.urls import path
from apps.student_management.views.teacher_view import *

urlpatterns = [
    path('teachers/', get_teachers_api),
    path('teachers/<int:pk>/', get_teacher),
    path('teachers/create/', create_teacher),
    path('teachers/update/<int:pk>/', update_teacher),
    path('teachers/delete/<int:pk>/', delete_teacher),
    path('teachers/<int:teacher_id>/assign-subject/<int:subject_id>/', assign_subject_to_teacher),
    path('teachers/<int:teacher_id>/remove-subject/<int:subject_id>/', remove_subject_from_teacher),
    path('teachers/<int:teacher_id>/assign-student/<int:student_id>/', assign_student_to_teacher),
    path('teachers/<int:teacher_id>/remove-student/<int:student_id>/', remove_student_from_teacher),
]
