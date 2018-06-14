
from django.conf.urls import url, include
from . import views
urlpatterns = [

    
    url('driveapp', views.index, name='index'),
]
