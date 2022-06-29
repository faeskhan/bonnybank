from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('rooms/', views.rooms, name="rooms"),
    path('promotions/', views.promotions, name="promotions"),
    path('events/', views.events, name="events"),
    path('contact/', views.contact, name="contact"),
]
