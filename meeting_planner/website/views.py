from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the meeting Place')


# Create your views here.
def date(request):
    return HttpResponse(f'This page was served at {datetime.now()}')


def about(request):
    return HttpResponse(f"Rishabh Jain \n 36 years\n Czech republic")
