from django.urls import path
from .views import showMeetingDetails, createNewMeeting, createNewRoom

urlpatterns = [
    path('<int:id>', showMeetingDetails, name='details'),
    path('newmeeting', createNewMeeting, name='newMeeting'),
    path('newroom', createNewRoom, name='newRoom')
]