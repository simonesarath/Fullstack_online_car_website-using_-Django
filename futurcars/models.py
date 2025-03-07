from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.model}"
    
    
class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=True)
    # test_drive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} booked {self.car.name} on {self.booking_date}"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"Message from visitors {self.name}"