from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('forms', my_form, name='forms'),
    path('edit_form/<int:user_id>/', edit_form, name='edit_form'),
    path('my_form/delete/<int:user_id>/', delete, name='delete'),
    path('form_up_img/', form_up_img, name='form_up_img'),
    path('form_up_img/delete_img/<int:img_id>/', delete_img, name='delete_img'),
    ]