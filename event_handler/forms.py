from django import forms 
from django.forms import ModelForm
from .models import Event,Participant


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

class TicketForm(forms.ModelForm):
    email=forms.TextInput()
    full_name=forms.Textarea()

    class Meta:
        model=Participant
        fields=['email',
                'full_name']

  