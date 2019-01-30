from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #AFTER A SUCCESSFUL SIGN UP, THE USER IS REVERSED BACK (REDIRECTED) TO THE LOGIN PAGE
    #IT IS reverse_lazy BECAUSE YOU DON'T WANT THIS TO EXECUTE UNTIL THE USER HAS HIT EXECUTE IN THE SIGN UP FORM
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
