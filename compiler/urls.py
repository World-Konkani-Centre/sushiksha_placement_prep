from django.urls import path, include
from . import views

app_name = 'compiler'

urlpatterns = [
    path('', views.code_editor, name = "compiler"),
    path('result/', views.result, name = "result"),
]