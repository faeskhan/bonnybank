from . models import Review, News
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages

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

def event_details(request, pk):
    return render(request, 'event_details')

def contact(request):
    return render(request, 'contact.html')

def news (request):
    media = News.objects.order_by('-date').all()

    page = request.GET.get('page')
    results = 1
    paginator = Paginator(media, results)

    try:
        media = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        media = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        media = paginator.page(page)

    
    context = {'media': media, 'paginator': paginator}
    return render (request, 'news.html', context)