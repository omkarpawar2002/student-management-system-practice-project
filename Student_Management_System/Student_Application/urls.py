from django.urls import path
from .views import ( create_student,show_student,update_student,delete_student )

urlpatterns = [
    path('create_stu/',create_student.as_view(),name='Create_Student'),
    path('show_stu/',show_student.as_view(),name='Show_Student'),
    path('update_stu/<int:pk>/',update_student.as_view(),name='Update_Student'),
    path('delete_stu/<int:pk>/',delete_student.as_view(),name='Delete_Student')
]