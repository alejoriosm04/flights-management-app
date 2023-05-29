from django.forms import ModelForm
from .models import Ticket

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
