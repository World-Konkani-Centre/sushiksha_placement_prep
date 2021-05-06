from django.urls import path
import mentors_panel.views as m_views

urlpatterns = [
    path('', m_views.mentors_home, name='mentors-home'),
    path('resume/', m_views.resume_list, name="resume-list"),
    path('resume/user/', m_views.resume_view_user, name="resume-view-user"),
    path('resume/<int:resumeId>', m_views.resume_view, name="resume-view"),
    path('interview/',m_views.interview_list,name='interview-list-mentor'),
    path('interview/<int:intId>',m_views.interview_details,name='interview-detail-mentor'),
    path('gd/', m_views.gd_list, name='gd-list-mentor'),
    path('gd/<int:intId>', m_views.gd_details, name='gd-detail-mentor'),

]
