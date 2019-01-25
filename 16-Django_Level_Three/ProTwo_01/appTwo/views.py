from django.shortcuts import render
# from django.http import HttpResponse
# from .models import User
# from . import forms
from appTwo.forms import UserForm


# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'appTwo/users.html',context=user_dict)

def createuser(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
            # user = User.objects.create(first_name=form.cleaned_data['first_name'],
            #                                   last_name=form.cleaned_data['last_name'],
            #                                   email=form.cleaned_data['email'])
            # user.save()
        else:
            print('ERROR FORM INVALID')
    return render(request,'appTwo/form_page.html',{'form':form })



    # return render(request,'appTwo/form_page.html',{'form':form})
