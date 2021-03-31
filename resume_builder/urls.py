from django.urls import path
import resume_builder.views as rb_views
urlpatterns = [
    path('', rb_views.test,name="test"),
]
