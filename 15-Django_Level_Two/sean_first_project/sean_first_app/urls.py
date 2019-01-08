from django.conf.urls import url
from sean_first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
