from . models import Review, News, Event, Promotions, Contact
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'index.html', context)

def about(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'about.html', context)

def rooms(request):
    return render(request, 'rooms.html')

def promotions(request):
    promotion = Promotions.objects.all()
    context = {'promotion': promotion}
    return render(request, 'promotions.html', context)

def events(request):
    function = Event.objects.order_by('-end').all()
    context = {'function': function}
    return render(request, 'events.html', context)

def event_details(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'event_details.html', context)

def contact(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        radio_button = request.POST['radio']
        day = request.POST['Day']
        month = request.POST['Month']
        year = request.POST['Year']
        nights = request.POST['of-Nights']
        message = request.POST['Message']

        # send_mail(subject, message, from_email, recipient_list)

        if radio_button == 'Booking':
            checkin = month +' '+ day +', '+ year
            checkout = nights + ' nights after checkin date'
            contact_obj = Contact(first_name = first_name, last_name=last_name, email=email, checkin=checkin, checkout=checkout, message=message)
            contact_obj.save()

        
        # print(checkin)
        # print(first_name)
        # print(last_name)
        # print(email)
        # print(radio_button)
        # print(day)
        # print(month) 
        # print(year)
        # print(nights)
        # print(message)
        return redirect('index')



    return render(request, 'contact.html')

def news (request):
    media = News.objects.order_by('-date').all()

    page = request.GET.get('page')
    results = 6
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