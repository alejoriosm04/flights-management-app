from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Flight, Ticket, Airline, Airport
from .forms import TicketForm


def flights(request):
    # implement a search thorugh id_vuelo or codigo_IATA_aerolinea_vuelo or categoria_vuelo
    searchTerm = request.GET.get('searchFlight', '')
    if searchTerm:
        flights = Flight.objects.filter(id_vuelo__icontains=searchTerm)
        if flights is None:
            flights = Flight.objects.filter(codigo_IATA_aerolinea_vuelo__icontains=searchTerm)
    else:
        flights = Flight.objects.all()
    return render(request, 'flights.html', {'searchTerm': searchTerm, 'flights': flights})


def detail(request, id_vuelo):
    flight = get_object_or_404(Flight, pk=id_vuelo) 
    #tickets = Ticket.objects.filter(id_vuelo_ticket=id_vuelo)
    tickets = Ticket.objects.all()
    return render(request, 'detail.html', {'flight': flight, 'tickets': tickets})


def about(request):
    return HttpResponse('<h1>Hello, world. You are at the ticket about.</h1>')


def bookflight(request, id_vuelo):
    flight = get_object_or_404(Flight, pk=id_vuelo)
    if request.method == 'GET':
        return render(request, 'bookflight.html', {'flight': flight, 'form': TicketForm(), 'flight': flight})
    else:
        try:
            form = TicketForm(request.POST)
            newTicket = form.save(commit=False)
            newTicket.save()
            return render(request, 'detail.html', {'flight': flight})
        except ValueError:
            return render(request, 'bookflight.html', {'form': TicketForm(), 'error': 'Bad data passed in. Try again.'})
