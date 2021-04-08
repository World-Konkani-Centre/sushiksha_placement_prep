from django.urls import path

from . import views

urlpatterns = [
    path('view/', views.interview_list, name='interviews-list'),
    path('view/<int:intId>', views.interview_details, name='interviews-single'),

]

