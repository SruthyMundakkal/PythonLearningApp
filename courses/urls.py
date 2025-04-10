from django.urls import path
from . import views

# courses/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('lesson/<int:id>/', views.lesson_detail, name='lesson-detail'),
    path('quiz/', views.quiz, name='quiz'),
    path('lesson/<int:lesson_id>/topics/', views.lesson_topics, name='lesson_topics'),
    path('topic/<int:topic_id>/details/', views.topic_detail, name='topic_detail'),
]
