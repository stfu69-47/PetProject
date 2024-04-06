from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('forms', my_form, name='forms'),
]

