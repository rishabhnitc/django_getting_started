from django.urls import path
from .views import detail, rooms_list, room, new_meet

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('new', new_meet, name='newmeet'),
    path('rooms', rooms_list, name='rooms'),
    path('rooms/<int:id>', room, name='room'),
    ]