from django.contrib import admin
from . models import Review, Event, News, Promotions, Contact

admin.site.register(Review)
admin.site.register(Event)
admin.site.register(News)
admin.site.register(Promotions)
admin.site.register(Contact)