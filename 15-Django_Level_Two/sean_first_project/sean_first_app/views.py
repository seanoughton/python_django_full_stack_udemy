from django.shortcuts import render
#functions that handle requests and return responses
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': "hello I am NEW from views.py!"}
    return render(request,'sean_first_app/index.html',context=my_dict)
    # return HttpResponse("Hello World!")



def help(request):
    my_dict = {'insert_me': "HELP PAGE"}
    return render(request,'sean_first_app/help.html',context=my_dict)
    # return HttpResponse("Hello World!")
