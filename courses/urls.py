from django.urls import path
from . import views

# courses/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('lesson/<int:lesson_id>/topics/', views.lesson_topics, name='lesson_topics'),
    path('topic/<int:topic_id>/details/', views.topic_detail_partial, name='topic_detail_partial'),
    path('contact/', views.contact, name='contact'),
    path('lesson/<int:id>/', views.lesson_detail, name='lesson-detail'),
    path('run_code/', views.run_code, name='run_code'),
    
]
