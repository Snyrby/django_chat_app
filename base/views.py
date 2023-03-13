from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RoomForm
from .models import Room

# Create your views here.

app_name = 'base'
def home_view(request, *args, **kwargs): # *args, **kwargs
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room_view(request, pk):
    room = Room.objects.get(id=pk)
    # .get will retrieve a single object
    # .filter will filter by particular field
    # .exclude will do the opposite of filter
    context = {'room': room}
    return render(request, 'base/rooms.html', context)

def create_room_view(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)



