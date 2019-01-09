from django.shortcuts import render
from django.http import HttpResponse
from userlist_app.models import User


def index(request):
    users_list = User.objects.order_by('last_name')
    users_dict = {'users':users_list}
    return render(request,"userlist_app/index.html",context=users_dict)
    # return HttpResponse('Hello World')
