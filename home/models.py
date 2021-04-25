from django.db import models


class Rooms(models.Model):
    room_name = models.CharField(max_length=50)
    room_num = models.IntegerField(default=1)
    floor_num = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.room_name}: Room {self.room_num} on {self.floor_num}'
        