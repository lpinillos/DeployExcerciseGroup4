from django.contrib import admin

# Register your models here.
from .models import Course, Professor

#Registro mis modelos para que se vean desde el admin
admin.site.register(Course)
admin.site.register(Professor)