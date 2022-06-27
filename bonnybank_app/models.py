from django.db import models
import uuid

class Review(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    quote = models.TextField(max_length=500) #Temporary value and change later for the card size    

    def __str__(self):
        return self.title

class Room(models.Model): # May want to include field to track which rooms are currently booked/available
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2) #Essentially must be greater than 0
    decription = models.TextField(max_length=2000)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/room')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "RoomImages"

class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    display_image = models.ImageField(upload_to='static/images/event')
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=600)
    source = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    display_image = models.ImageField(upload_to='static/images/news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"

class Promotions(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Promotions"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)
    checkin = models.DateTimeField(blank=True, null=True)
    checkout = models.DateTimeField(blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title