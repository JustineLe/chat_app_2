from django.urls import path
from . import views


urlpatterns = [
    path('', views.room, name='room'),
    path('<slug:slug>/', views.room_detail, name='room_detail'),
]