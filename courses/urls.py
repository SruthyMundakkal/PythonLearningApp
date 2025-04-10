from django.urls import path
from . import views

# courses/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('lesson/<int:id>/', views.lesson_detail, name='lesson-detail'),
    path('quiz/', views.quiz, name='quiz'),
]
