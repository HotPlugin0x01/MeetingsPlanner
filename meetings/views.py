from django.shortcuts import render, get_object_or_404
from .models import Meetings


def showMeetingDetails(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, 'meetings/meetingDetails.html', {'meeting':meeting})

