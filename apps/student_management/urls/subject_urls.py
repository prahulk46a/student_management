from django.urls import path
from apps.student_management.views.subject_view import *

urlpatterns = [
    path('subjects/', get_subjects_api),
    path('subjects/<int:pk>/', get_subject),
    path('subjects/create/', create_subject),
    path('subjects/update/<int:pk>/', update_subject),
    path('subjects/delete/<int:pk>/', delete_subject),
]
