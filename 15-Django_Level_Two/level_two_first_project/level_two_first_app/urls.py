from django.conf.urls import url
from level_two_first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]
