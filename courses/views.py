from django.shortcuts import render, get_object_or_404
from .models import Lesson, Topic, Quiz
from django.http import JsonResponse  # Add this import

def home(request):
    lessons = Lesson.objects.all()
    return render(request, 'courses/home.html', {
        'lessons': lessons
    })

def lesson_detail(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})


def lesson_topics(request, lesson_id):
    topics = Topic.objects.filter(lesson_id=lesson_id).values('title')
    return JsonResponse(list(topics), safe=False)

def quiz(request):
    quizzes = Quiz.objects.select_related('topic').all()
    return render(request, 'courses/quiz.html', {
        'quizzes': quizzes
    })
