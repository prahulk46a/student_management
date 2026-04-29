from django.urls import path
from apps.student_management.views.course_view import *

urlpatterns = [
    path('courses/', get_courses_api),
    path('courses/<int:pk>/', get_course),
    path('courses/create/', create_course),
    path('courses/update/<int:pk>/', update_course),
    path('courses/delete/<int:pk>/', delete_course),
]
