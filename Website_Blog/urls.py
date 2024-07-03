from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from source import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods-web/', views.show_food, name='foods_web'),
    path('exercises-web/', views.show_exercise, name='exercises_web'),
    path('start_web/', views.start_web, name="start_web")
]

