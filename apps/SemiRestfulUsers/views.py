from django.shortcuts import render, HttpResponse, redirect
import re
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random, string, math
from models import *
from django.core.urlresolvers import reverse
from django.contrib.messages import *
def index(request):
    context = {'users':User.objects.all()}

    return render(request,'SemiRestfulUsers/index.html', context)

def new(request):
    # commands for the database
    # first_name = request.POST["first_name"]
    # last_name = request.POST["last_name"]
    # User.objects.create(first_name=first_name,last_name=last_name,email=request.POST["email"])
    return render(request,'SemiRestfulUsers/new_user.html')

def create(request):
    errors = User.objects.is_valid(request.POST)
    info = User.objects.all()
    if len(errors)!=0:
        messages.add_message(request, INFO,"Must be valid email!")
        return redirect('/users/new')
    else:
        for i in info:
            if (request.POST["email"]==i.email):
                messages.add_message(request, INFO,"email already exists! Try logging in")

                return redirect('/users/new')
        User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],email=request.POST["email"])

    return redirect('/users')

def edit(request, user_id):
    user = {'user': User.objects.get(id=user_id)}
    edit = True
    print edit
    return render(request,'SemiRestfulUsers/edit_user.html', user, edit)
    # return redirect(reverse('my_edit'))

def show(request, user_id):
    user = {'user': User.objects.get(id=user_id)}
    edit = False
    print edit
    return render(request,'SemiRestfulUsers/show_user.html', user, edit)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()

    return redirect('/users')
