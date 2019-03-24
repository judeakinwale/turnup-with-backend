from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.all_events, name='events'),
    path('about/', views.about, name='about'),
]