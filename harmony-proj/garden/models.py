from django.db import models

URGENCY_CHOICES = [
    ("highest", "high", "medium", "low"),
]

TYPE_CHOICES = [
    ("code", "write", "speak", "order"),
]

class Task(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateTimeField('due')
    urgency = models.CharField(max_length=50, choices=URGENCY_CHOICES)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)