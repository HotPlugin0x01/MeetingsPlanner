from django.shortcuts import render, get_object_or_404, redirect
from .models import Meetings
from home.models import Rooms
from django.forms import modelform_factory


def showMeetingDetails(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, 'meetings/meetingDetails.html', {'meeting':meeting})


def createNewMeeting(request):
    MeetingsForm = modelform_factory(Meetings, exclude=[])   # Creating form class from model fields

    # Check if form is submitted
    if request.method == 'POST':
        form = MeetingsForm(request.POST)  # Form object from filled data
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeetingsForm()   # Form object
    return render(request, 'meetings/newMeeting.html', {'form': form})
