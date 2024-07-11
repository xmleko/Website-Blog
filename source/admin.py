from django.contrib import admin
from .models import Food
from .models import Exercise
from .models import LooseWrite

admin.site.register(Food)
admin.site.register(Exercise)
admin.site.register(LooseWrite)
