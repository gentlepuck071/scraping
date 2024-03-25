from django.urls import path
from . import views

urlpatterns = [
    path('web3events/', views.event_list, name = 'event_list'),
    path('web3events/<int:pk>/', views.event_detail, name = 'event_detail'),
]