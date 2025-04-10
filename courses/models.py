from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Topic(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Quiz(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
