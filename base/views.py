from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets Learn Python!'},
    {'id': 2, 'name': 'Lets learn SQL!'},
]

def home_view(request, *args, **kwargs): # *args, **kwargs
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room_view(request, *args, **kwargs):
    return render(request, 'base/room.html', {})

