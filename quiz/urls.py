from django.urls import path

from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, QuizUserProgressViewAdmin, VkssfQuizListView, apti_home_page

urlpatterns = [
    
    path('', apti_home_page, name='quiz_index'),

    path('practice-tests',
         view=QuizListView.as_view(),
         name='practice_tests'),

    path('vkssf-tests',
         view=VkssfQuizListView.as_view(),
         name='vkssf_test'),

    path('category/',
         view=CategoriesListView.as_view(),
         name='quiz_category_list_all'),

    path('category/<str:category_name>',
         view=ViewQuizListByCategory.as_view(),
         name='quiz_category_list_matching'),

    path('progress/',
         view=QuizUserProgressView.as_view(),
         name='quiz_progress'),

    path('marking/',
         view=QuizMarkingList.as_view(),
         name='quiz_marking'),

    path('marking/<int:pk>/',
         view=QuizMarkingDetail.as_view(),
         name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    path('<slug:slug>/',
         view=QuizDetailView.as_view(),
         name='quiz_start_page'),

    path('<str:quiz_name>/take/',
         view=QuizTake.as_view(),
         name='quiz_question'),

    path('progress/<int:id>',
         view=QuizUserProgressViewAdmin.as_view(),
         name='quiz_progress-admin'),
]
