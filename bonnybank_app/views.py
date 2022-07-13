from . models import Review, News, Event, Promotions
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from . forms import ContactForm

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
    # form = ContactForm()

    if request.method == 'POST':
        
        # form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'], 
                'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect (":index")

    context = {'form': form}
    return render(request, 'contact.html', context)

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