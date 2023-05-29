from django.contrib import admin
from .models import Flight, Airline, Airport, City, Country, Ticket

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Ticket)