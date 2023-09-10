from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from courses.models import Course



@method_decorator(login_required, name='dispatch')
class CoursesMain(View):

    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses_main.html', {
            'courses':courses
        })
    
    def signout(request):
        logout(request)
        return redirect("/signin")
        
    