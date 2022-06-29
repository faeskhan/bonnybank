from . models import Review
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def rooms(request):
    return render(request, 'rooms.html')

def promotions(request):
    return render(request, 'promotions.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')