from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    people=models.IntegerField()
    message = models.TextField()

class Info(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      subject=models.CharField(max_length=100)
      message = models.TextField()