from django.db import models
   
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Topic(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=255)
    content = models.TextField()  # TextField already allows large content, so no need to change this
    code_snippet = models.TextField(blank=True, null=True)  # New field for optional code

    def __str__(self):
        return self.title

class Quiz(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    correct_answer = models.TextField()
    option_1 = models.TextField(default='Default Option 1')  # Add default value here
    option_2 = models.TextField(default='Default Option 2')
    option_3 = models.TextField(default='Default Option 3')
    option_4 = models.TextField(default='Default Option 4')

    def __str__(self):
        return self.question

