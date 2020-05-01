from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {'message': ' This data was sent from the view to the template.',
                  # "num_meetings": Meeting.objects.count()}

                   "meetings": Meeting.objects.all()}
                  )


# Create your views here.
def date(request):
    return HttpResponse(f'This page was served at {datetime.now()}')


def about(request):
    return HttpResponse(f"Rishabh Jain \n 36 years\n Czech republic")
