from django import forms 
from django.forms import ModelForm
from .models import Event 


class EventForm(ModelForm):

    class Meta:
        model=Event
        fields=[
            'name',
            'event_date',
            'number_of_participant',
            'fylier',
            
        ]
        event_date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])
        # widgets = {
        # 'publisher':forms.TextInput(attrs={'class':'form-control','readonly':True}),
        # }

class TicketForm(forms.Form):
    email=forms.TextInput()
    full_name=forms.TextInput()

  