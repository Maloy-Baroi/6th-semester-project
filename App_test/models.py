from django.db import models


# Create your models here.
class MCQ(models.Model):
    question = models.CharField(max_length=254)
    option1 = models.CharField(max_length=254)
    option2 = models.CharField(max_length=254)
    option3 = models.CharField(max_length=254)
    option4 = models.CharField(max_length=254)
    correct_answer = models.CharField(max_length=254)

