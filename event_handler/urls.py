from django.urls import path

from .views import EventList,EventDetail,EventCreate,ticketView,TicketCreate

app_name='event_handler'
urlpatterns = [
   path('',EventList.as_view(),name='event_list'),
   path('event/<slug:slug>/create/',ticketView,name='event_create'),
   # path('event/<slug:slug>/create/',EventCreate.as_view(),name='event_create'),
   # path('ticket/',TicketCreate.as_view(),name='event_create'),
   path('<slug:slug>/',EventDetail.as_view(),name='event_detail'),
]
