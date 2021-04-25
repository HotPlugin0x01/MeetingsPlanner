from django.urls import path
from .views import showMeetingDetails

urlpatterns = [
    path('<int:id>', showMeetingDetails, name='details')
]