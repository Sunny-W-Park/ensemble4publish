from django.urls import path
from django.conf.urls import include
from team import views

urlpatterns = [path('', views.team, name = 'team')]
