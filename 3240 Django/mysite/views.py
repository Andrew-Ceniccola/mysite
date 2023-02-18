from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    NAME = "Homepage"
    return render(request, 'homepage.html', {'name':NAME})