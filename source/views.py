from django.shortcuts import render
from .models import Food
from .models import Exercise
from django.shortcuts import render, get_object_or_404
from .models import LooseWrite

def start_web(request):
    loose = LooseWrite.objects.all()
    loose_last_write = LooseWrite.objects.all().order_by('-id')[:3]
    return render(request, 'start_web.html', {'loose': loose, 'loose_last_write': loose_last_write})

def start_web_get_last_write(request):
    loose_last_write = LooseWrite.objects.all().order_by('-id')[:3]
    return render(request, 'start_web.html', {'loose_last_write': loose_last_write})

def show_loose(request):
    loose = LooseWrite.objects.all()
    return render(request, 'loose_web.html', {'loose': loose})

def show_food(request):
    foods = Food.objects.all()
    return render(request, 'foods_web.html', {'foods' : foods})

def show_exercise(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises_web.html', {'exercises': exercises})

def post_detail(request, id):
    post = get_object_or_404(LooseWrite, id=id)
    return render(request, 'loose_web.html', {'post': post})
