from django.shortcuts import render
#functions that handle requests and return responses
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")
