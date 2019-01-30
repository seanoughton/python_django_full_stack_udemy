# from django.config.urls import url
from django.contrib.auth import views as auth_views
#DJANGO HAS A LOGIN AND LOGOUT VIEW AND THIS IS HOW YOU ACCCESS THEM
#YOU DO NOT HAVE TO CREATE THOSE IN YOUR VIEWS.PY FILE
from . import views
from django.urls import path,include

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name="login"),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('signup/', views.SignUp.as_view(),name="signup"),
]
