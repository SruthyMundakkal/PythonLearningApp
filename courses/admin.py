from django.contrib import admin
from .models import Lesson, Topic, Quiz

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1

class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [TopicInline]

class TopicAdmin(admin.ModelAdmin):
    inlines = [QuizInline]

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Quiz)
