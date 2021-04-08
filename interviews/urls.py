from django.urls import path

from . import views

urlpatterns = [
    path('gd/', views.interview_list, name='gd-interviews-list'),
    path('gd/<int:intId>', views.interview_list, name='gd-interviews-single'),
    path('view/', views.interview_list, name='interviews-list'),
    path('view/<int:intId>', views.interview_details, name='interviews-single'),
]

