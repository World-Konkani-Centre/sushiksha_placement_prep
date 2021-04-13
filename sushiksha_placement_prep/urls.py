from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import resume_builder.urls as builder_url
import mentors_panel.urls as mentor_url
import quiz.urls as assmt_url
from sushiksha_placement_prep import settings
import interviews.urls as int_urls
import users.urls as user_url
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    url('users/', include(user_url)),
    url('resume-builder/', include(builder_url)),
    url('mentors/', include(mentor_url)),
    url('assessment/', include(assmt_url)),
    url('interview/', include(int_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
