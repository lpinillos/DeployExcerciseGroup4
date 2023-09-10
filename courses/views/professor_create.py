from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from courses.forms.create_professor_form import CreateProfessorForm


class ProfessorCreate(View):
    def get(self, request):
        return render(request, 'professor_create.html', {
            'form':CreateProfessorForm
        })
    def post(self, request):
        form = CreateProfessorForm(request.POST)
        form.save()
        return redirect("/")
    
    