from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RoomForm
from .models import Room, Topic, Message
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

app_name = 'base'
# don't name this login because it is a builtin function


# both in login and register it passes in the page. If the page is login, then it will show the login form
# if the page is register, then it will show the register form
def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # this will save the form but freeze it in time
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base/login_register.html', {'form': form,})


def home_view(request, *args, **kwargs): # *args, **kwargs
    # This is how to search for something in the database with a search bar etc.
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    # you could change this to show only people you follow etc.
    room_messages = Message.objects.all().filter(Q(Room__topic__name__icontains=q))
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)


def room_view(request, pk):
    room = Room.objects.get(id=pk)
    # .get will retrieve a single object
    # .filter will filter by particular field
    # .exclude will do the opposite of filter
    # messgaes = parent. child _set.all() - infront of created_at means descending order
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        new_message = Message.objects.create(
            user=request.user,
            Room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('rooms', pk=room.id)


    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/rooms.html', context)

def user_profile(request, pk):
    user = User.objects.get(id=pk)
    # gets all the children values when using 'model name' _set then all
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'topics': topics, 'room_messages': room_messages}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def create_room_view(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.hosts = request.user
            room.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def update_room_view(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    # this validates if the user can edit a room or not. Even if knowing the url
    if request.user != room.hosts:
        return HttpResponse('You are not allowed to edit this room')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def delete_room_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.hosts:
        return HttpResponse('You are not allowed to edit this room')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='login')
def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed to edit this message')
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})
