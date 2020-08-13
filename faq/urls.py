from django.urls import path
from django.conf.urls import include
from faq import views

urlpatterns = [path('', views.faq, name = 'faq')]
