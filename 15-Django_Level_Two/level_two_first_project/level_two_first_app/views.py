from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': 'HELLO I AM FROM LEVEL TWO FIRST APP'}
    return render(request,'level_two_first_app/index.html',context=my_dict)
