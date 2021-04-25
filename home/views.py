from django.shortcuts import render
from meetings.models import Meetings


def home(request):
    return render(request, 'home/home.html', {'meetings': Meetings.objects.all()})