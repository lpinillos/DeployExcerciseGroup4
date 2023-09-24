from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from courses.models import Course
from django.db.models import Q
from courses.util.query_util import get_courses_by_query




@method_decorator(login_required, name='dispatch')
class CoursesMain(View):

    def get(self, request):
        query = request.GET.get('q', '')
        courses = get_courses_by_query(query)
        return render(request, 'courses_main.html', {
            'courses': courses,
        })
        
    
    def signout(request):
        logout(request)
        return redirect("/signin")
        
    