from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    hosts = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    # auto_now_add is the method used to only add the time on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now is the method used to create the time on update every time
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    # create a string representation of the room
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # this creates a foreign key to the room and will set null if the room is deleted
    # Rooms = models.ForeignKey(Rooms, on_delete=models.set_null)
    # this creates a foreign key to the room and will remove all messages if the room is deleted
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    # auto_now_add is the method used to only add the time on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now is the method used to create the time on update every time
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.body[0:50]
