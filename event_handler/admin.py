from django.contrib import admin
from .models import Publisher,Event,Participant
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Event)
admin.site.register(Participant)