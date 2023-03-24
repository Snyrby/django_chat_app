from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),

    path('', views.home_view, name='home'),
    path('rooms/<str:pk>/', views.room_view, name='rooms'),
    path('profile/<str:pk>/', views.user_profile, name='user-profile'),
    path('create-room/', views.create_room_view, name='create-room'),
    path('update-room/<str:pk>/', views.update_room_view, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_room_view, name='delete-room'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete-message'),
    path('update-user/', views.update_user, name='update-user'),
    path('topics/', views.topics_page, name='topics'),
]
