from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('rooms/<str:pk>/', views.room_view, name='rooms'),
    path('create-room/', views.create_room_view, name='create-room'),
]
