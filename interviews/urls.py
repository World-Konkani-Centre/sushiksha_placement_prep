from django.urls import path

from . import views

urlpatterns = [
    path('gd/', views.gd_apply, name='gd-interviews-list'),
    path('gd/<int:intId>', views.gd_interview_details, name='gd-single'),
    path('view/', views.interview_list, name='interviews-list'),
    path('view/<int:intId>', views.interview_details, name='interviews-single'),
]

