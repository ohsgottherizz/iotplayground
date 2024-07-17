from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='reservations')
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.child.name} - {self.time}"

class PlaygroundOccupancy(models.Model):
    level = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Occupancy: {self.level}% at {self.timestamp}"