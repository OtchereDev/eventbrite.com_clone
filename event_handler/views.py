from django.shortcuts import render
from django.views.generic import (ListView,DetailView,CreateView,
                                    DeleteView,UpdateView)

from .models import Event,Participant
from .forms import EventForm,TicketForm
from django.http import Http404

class EventList(ListView):
    template_name='event_list.html'
    context_object_name='events'
    model= Event

class EventDetail(DetailView):
    template_name='event_detail.html'
    context_object_name='event'
    model=Event

class EventCreate(CreateView):
    template_name='event_create.html'
    form_class=EventForm
    model=Event
    success_url='/'

    def form_valid(self,form):
        form_done=form.save(commit=False)
        form_done.publisher=self.request.user           
        return super().form_valid(form)



class TicketCreate(CreateView):
    template_name='ticket.html'
    form_class=TicketForm
    model=Participant
    success_url='/'

    # form.instance.story = Story.objects.get(slug=self.kwargs['slug'])
    # print(Event.objects.filter(slug=self.kwargs['slug']).exists())

    # def get(self, request):
    #     if Event.objects.filter(slug=self.kwargs['slug']).exists():
       
    #         return super().get(request)
    #     else:
    #         return Http404

    def form_valid(self,form):
        form_done=form.save(commit=False)
        form_done.publisher=self.request.user           
        return super().form_valid(form)
