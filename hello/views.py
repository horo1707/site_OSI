from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def birds_facts(request):
    return render(request, "birds_facts.html")

def popug1(request):
    return render(request, "popug1.jpg")

