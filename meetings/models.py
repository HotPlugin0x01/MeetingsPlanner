from django.db import models
from datetime import time
from home.models import Rooms

# Create your models here.
class Meetings(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    start_time = models.TimeField(time(8))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} at {self.start_time} on {self.date}'
