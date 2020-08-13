from django.urls import path
from django.conf.urls import include
from daemun import views

urlpatterns = [path('', views.daemun, name = 'daemun'),]
