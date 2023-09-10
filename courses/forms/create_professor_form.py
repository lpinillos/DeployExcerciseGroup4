from django.forms import ModelForm
from courses.models import Course, Professor

class CreateProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['name','major']