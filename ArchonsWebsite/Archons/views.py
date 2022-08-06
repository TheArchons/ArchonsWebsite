from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def socials(request):
    return render(request, 'socials.html')

def robots(request):
    return render(request, 'robots.txt')

def projects(request):
    return render(request, 'projects.html')