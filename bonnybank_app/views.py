from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def rooms(request):
    return render(request, 'rooms.html')