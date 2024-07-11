from django.db import models
from django.utils import timezone

class Food(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    ingredients = models.TextField(max_length=100)
    description = models.TextField(max_length=400)

class Exercise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    difficult_level = models.CharField(max_length=20)
    description = models.TextField(max_length=400)

class LooseWrite(models.Model):
    id = models.IntegerField(primary_key=True)
    logo = models.ImageField(upload_to='logos/', null = True)
    title = models.CharField(max_length=90)
    short_description = models.CharField(max_length=40)
    author = models.CharField(max_length=30, default=0)
    data = models.DateTimeField(default=timezone.now)
    description1 = models.TextField(max_length=400)
    description2 = models.TextField(max_length=400)
    description3 = models.TextField(max_length=400)
    description4 = models.TextField(max_length=400)
    description5 = models.TextField(max_length=400)
    description6 = models.TextField(max_length=400)


