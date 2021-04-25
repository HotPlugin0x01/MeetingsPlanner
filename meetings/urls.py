from django.urls import path
from .views import showMeetingDetails, createNewMeeting

urlpatterns = [
    path('<int:id>', showMeetingDetails, name='details'),
    path('NewMeeting', createNewMeeting, name='newMeeting')
]