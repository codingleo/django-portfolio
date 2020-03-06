from django.shortcuts import render
from django.http import HttpRequest

from .models import Job

# Create your views here.

def home(request: HttpRequest):
    jobs = list(Job.objects.all())
    print(jobs)
    
    return render(request, "jobs/home.html", {"jobs": jobs})