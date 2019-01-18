from django.shortcuts import render
from . import forms


def index(request):
    return render(request,'seanformapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("name:" + form.cleaned_data['name'])
            print("email:" + form.cleaned_data['email'])
            print("text:" + form.cleaned_data['text'])

    return render(request,'seanformapp/form_page.html',{'form':form})
