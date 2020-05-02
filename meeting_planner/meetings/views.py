from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory
# Create your views here.
from .models import Meeting, Room
from .forms import MeetingForm
#MeetingForm = modelform_factory(Meeting, exclude=[])


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



def new_meet(request):
    if(request.method == "POST"):
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    
    return render(request, "meetings/new.html",
        {"form":form})
