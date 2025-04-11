from django.shortcuts import render, get_object_or_404

from courses.forms import ContactForm
from .models import Lesson, Topic, Quiz
from django.http import JsonResponse 
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render
from django.http import JsonResponse
import sys
import io
import sys
from django.shortcuts import get_object_or_404


def home(request):
    lessons = Lesson.objects.all()
    return render(request, 'courses/home.html', {
        'lessons': lessons
    })

def lesson_detail(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})

def topic_detail_partial(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'courses/lesson_detail.html', {'topic': topic})


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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email (make sure to configure your email settings in settings.py)
            send_mail(
                f"Message from {name}: {subject}",
                message,
                email,
                [settings.CONTACT_EMAIL],  # Set this in your settings.py
            )

            # Redirect to a success page or display a success message
            return render(request, 'courses/contact_success.html')

    else:
        form = ContactForm()

    return render(request, 'courses/contact.html', {'form': form})

def run_code(request, topic_id):
    if request.method == "POST":
        code_snippet = request.POST.get("code_snippet", "")
        print(f"Received code: {code_snippet}")  # For debugging
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()

        # Only allow 'print' from built-ins
        safe_globals = {"__builtins__": {"print": print}}

        try:
            exec(code_snippet, safe_globals)
            output = redirected_output.getvalue()
            print(f"Output: {output}")  # For debugging
        except Exception as e:
            output = f"Error: {str(e)}"
        finally:
            sys.stdout = old_stdout

        return JsonResponse({"output": output})

    return JsonResponse({"error": "Invalid request method"}, status=405)




