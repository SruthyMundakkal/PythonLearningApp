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


def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        lesson = topic.lesson
        # Return the details of the topic as a JSON response
        return JsonResponse({
            'title': topic.title,
            'content': topic.content,  # Add any other relevant fields
            'code_snippet': topic.code_snippet  # Add code snippet if necessary
        })
    except Topic.DoesNotExist:
        return JsonResponse({'error': 'Topic not found'}, status=404)
    
    
def quiz(request):
    quizzes = Quiz.objects.select_related('topic').all()
    if request.method == 'POST':
        score = 0
        quiz_results = []
        for quiz in quizzes:
            answer = request.POST.get(f'question_{quiz.id}')
            is_correct = answer == quiz.correct_answer  # Check if answer is correct
            if is_correct:
                score += 1
            # Store the quiz, the selected answer, and the correct answer
            quiz_results.append({
                'question': quiz.question,
                'selected_answer': answer,
                'correct_answer': quiz.correct_answer,
                'is_correct': is_correct
            })
        
        return render(request, 'courses/quiz_result.html', {
            'score': score,
            'total': len(quizzes),
            'quiz_results': quiz_results  # Pass quiz results to the template
        })
    return render(request, 'courses/quiz.html', {'quizzes': quizzes})
