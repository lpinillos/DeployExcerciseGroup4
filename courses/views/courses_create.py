from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from courses.forms.create_course_form import CreateCourseForm


class CoursesCreate(View):
    def get(self, request):
        return render(request, 'courses_create.html', {
            'form':CreateCourseForm
        })
    def post(self, request):
        form = CreateCourseForm(request.POST)
        form.save()
        return redirect("/")
    
    