from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.award_badge, name="badge"),
]
