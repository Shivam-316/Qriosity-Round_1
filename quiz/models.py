from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.TextField()
    answer=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.question[:50]}...'