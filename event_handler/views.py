from django.shortcuts import render
from django.views.generic import (ListView,DetailView,CreateView,
                                    DeleteView,UpdateView)

from .models import Event,Participant
from .forms import EventForm,TicketForm
from django.http import HttpResponse,HttpResponseNotFound,Http404
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



def ticketView(request,slug):
    if  not Event.objects.filter(slug=slug).exists():
        raise Http404
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form_done=form.save(commit=False)
        form_done.event_reg=Event.objects.get(slug=slug)    
        form_done.save()
    context={
        'form':form
    }
    print(form)
    return render(request,'ticket.html',context)