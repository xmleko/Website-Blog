from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from source import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods-web/', views.show_food, name='foods_web'),
    path('exercises-web/', views.show_exercise, name='exercises_web'),
    path('start_web/', views.start_web, name="start_web"),
    path('loose_web/', views.show_loose, name="loose_web")
]


