from django.urls import path, include
from . import views

app_name = 'compiler'

urlpatterns = [
    path('all',views.q_all,name="questions"),
    path('problem/<int:qid>',views.question_single,name="question-single"),
    path('category/<int:cid>',views.category,name="q-category"),
    path('subcategory/<int:scid>',views.subcategory,name="q-sub-category"),
    #path('', views.code_editor, name="compiler"),
    path('result/<int:id>', views.result, name="result"),
    path('result/',views.resultt, name="result2")
]
