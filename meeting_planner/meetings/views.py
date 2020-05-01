from django.shortcuts import render, get_object_or_404

# Create your views here.
from meetings.models import Meeting, Room


def detail(request, id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html",
                  {'meeting': meeting})

def room(request, id):
    #meeting = Meeting.objects.get(pk=id)
    room_details = get_object_or_404(Room, pk=id)
    return render(request, "meetings/roomdetail.html",
                  {'room': room_details})

def rooms_list(request):
    #meeting = Meeting.objects.get(pk=id)
    rooms = Room.objects.all()
    print(rooms)
    return render(request, "meetings/rooms.html",
                  {'rooms': rooms})
