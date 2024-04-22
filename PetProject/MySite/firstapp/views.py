from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.


def index(request):
    context = {
        'text': 'Test form'
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'firstapp/about.html')


def contacts(request):
    return render(request, 'firstapp/contacts.html')


def my_form(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            # name = userform.cleaned_data.get('name')
            # age = userform.cleaned_data.get('age')
            # return HttpResponse(f'<h2>Name and age are corrected - {name}, {age} years old.</h2>')
            userform.save()
            return redirect('index')
    userform = UserForm()
    context = {
        'form': userform
    }
    return render(request, 'firstapp/my_form.html', context)