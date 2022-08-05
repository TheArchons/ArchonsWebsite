from django.shortcuts import render
from django.http import HttpResponse
from os import getcwd

# Create your views here.
def index(request):
    print(getcwd())
    return render(request, 'index.html')

def robots(request):
    return render(request, 'templates/robots.txt')