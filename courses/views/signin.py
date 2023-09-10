from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from courses.forms.create_course_form import CreateCourseForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


class Signin(View):
    def get(self, request):
        return render(request, 'signin.html', {
            'form':AuthenticationForm
        })
    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return HttpResponse('No existe el usuario') 
        else:
            login(request, user)
            return redirect("/")
    
    