from django.urls import path

from . import views

urlpatterns = [
    path('', views.interview_home, name='interview-home'),
    path('gd/', views.gd_apply, name='gd-interviews-list'),
    path('gd/<int:intId>', views.gd_interview_details, name='gd-single'),
    path('tech/view/', views.interview_list, name='interviews-list'),
    path('tech/view/<int:intId>', views.interview_details, name='interviews-single'),
    path('hr/view/', views.hr_interview_list, name='hr-interviews-list'),
    path('hr/view/<int:intId>', views.hr_interview_details, name='hr-interviews-single'),
    path('counselling/view/', views.counselling_list, name='counselling-list'),
    path('counselling/view/<int:intId>', views.counselling_details, name='counselling-single'),
]

