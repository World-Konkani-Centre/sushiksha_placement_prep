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
import language.urls as l_urls
import  compiler.urls as c_urls
import badge.urls as b_urls

handler404 = 'sushiksha_placement_prep.views.handler404'
handler500 = 'sushiksha_placement_prep.views.handler500'
handler400 = 'sushiksha_placement_prep.views.handler400'
handler403 = 'sushiksha_placement_prep.views.handler403'

urlpatterns = [
    path('', index, name='index'),
    path('grappelli/', include('grappelli.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    url('users/', include(user_url)),
    url('resume-builder/', include(builder_url)),
    url('mentors/', include(mentor_url)),
    url('aptitude/', include(assmt_url)),
    url('language/', include(l_urls)),
    url('interview/', include(int_urls)),
    url('problemset/', include(c_urls)),
    url('award-badge/', include(b_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
