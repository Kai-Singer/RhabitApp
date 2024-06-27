from django.urls import path
from rhabitApp import views

urlpatterns = [
  path('', views.home, name = 'home')
]