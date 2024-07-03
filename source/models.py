from django.db import models

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


