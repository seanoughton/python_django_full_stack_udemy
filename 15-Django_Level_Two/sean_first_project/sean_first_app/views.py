from django.shortcuts import render
#functions that handle requests and return responses
from django.http import HttpResponse
from sean_first_app.models import Topic,Webpage,AccessRecord

def index(request):
    #objects must be a query to the database through the orm
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'sean_first_app/index.html',context=date_dict)
