from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)
from . import models


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #this provides you with a record of every school in this table



class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School






class IndexView(TemplateView):
    template_name = "index.html"

    #this creates the context dictionary
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context




# from django.http import HttpResponse

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class based views are cool!")
