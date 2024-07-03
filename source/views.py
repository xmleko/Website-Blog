from django.shortcuts import render
from .models import Food
from .models import Exercise

def start_web(request):
    return render(request, 'start_web.html')
def show_food(request):
    foods = Food.objects.all()
    return render(request, 'foods_web.html', {'foods' : foods})

def show_exercise(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises_web.html', {'exercises': exercises})
