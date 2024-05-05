from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import *
from .models import *


def index(request):
    people_quantity = Person.object_person.count()
    context = {
        'text': 'Main page',
        'people_quantity': people_quantity
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'firstapp/about.html')


def contacts(request):
    return render(request, 'firstapp/contacts.html')


def edit_form(request, user_id):
    person = Person.object_person.get(id=user_id)
    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return redirect('forms')
    data = {'person': person}
    return render(request, 'firstapp/edit_form.html', context=data)


def delete(request, user_id):
    try:
        person = Person.object_person.get(id=user_id)
        person.delete()
        return redirect('firstapp/my_form.html')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Object not found</h2>')


def my_form(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('firstapp/my_form.html')
    my_text = 'Intelligence of users'
    people = Person.object_person.all()
    people_quantity = people.count()
    userform = UserForm()
    context = {
        'form': userform,
        'people': people,
        'my_text': my_text,
        'people_quantity': people_quantity,
    }
    return render(request, 'firstapp/my_form.html', context)


def form_up_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Saved images'
    my_img = Image.obj_img.all()
    form = ImageForm()
    context = {
        'my_text': my_text,
        'my_img': my_img,
        'form': form,
    }
    return render(request, 'firstapp/form_up_img.html', context)


def delete_img(request, img_id):
    try:
        img = Image.obj_img.get(id=img_id)
        img.delete()
        return redirect('firstapp/form_up_img.html')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Object not found</h2>')