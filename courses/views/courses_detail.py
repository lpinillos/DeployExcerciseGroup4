from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View


class CoursesMain(View):
    
    def get(self, request):
        return render(request, 'courses_main.html')
    
    