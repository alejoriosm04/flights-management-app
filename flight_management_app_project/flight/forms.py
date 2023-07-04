from django.forms import ModelForm
from .models import Ticket, Flight

class TicketForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['id_ticket'].widget.attrs.update({'class': 'form-control'})
        self.fields['grupo'].widget.attrs.update({'class': 'form-control'})
        self.fields['asiento'].widget.attrs.update({'class': 'form-control'})
        self.fields['categoria_pasajero'].widget.attrs.update({'class': 'form-control'})
        self.fields['equipaje_mano'].widget.attrs.update({'class': 'form-control'})
        self.fields['equipaje_bodega'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Ticket
        fields = ['id_ticket', 'grupo', 'asiento', 'categoria_pasajero', 'equipaje_mano', 'equipaje_bodega']
        labels = {
            'id_ticket': 'Ticket ID',
            'grupo': 'Group',
            'asiento': 'Seat',
            'categoria_pasajero': 'Passenger Category',
            'equipaje_mano': 'Hand Luggage',
            'equipaje_bodega': 'Hold Luggage'
        }


class FlightForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['id_vuelo'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_IATA_aerolinea_vuelo'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_IATA_aeropuerto_salida'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_ciudad_aeropuerto_salida'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_pais_aeropuerto_salida'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_IATA_aeropuerto_llegada'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_ciudad_aeropuerto_llegada'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_pais_aeropuerto_llegada'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_salida'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_llegada'].widget.attrs.update({'class': 'form-control'})
        self.fields['categoria_vuelo'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Flight
        fields = ['id_vuelo', 'codigo_IATA_aerolinea_vuelo', 'codigo_IATA_aeropuerto_salida', 'id_ciudad_aeropuerto_salida', 'id_pais_aeropuerto_salida', 'codigo_IATA_aeropuerto_llegada', 'id_ciudad_aeropuerto_llegada', 'id_pais_aeropuerto_llegada', 'fecha_salida', 'fecha_llegada', 'categoria_vuelo']