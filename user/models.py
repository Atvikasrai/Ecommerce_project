from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#-------------------------------Model for Customer Profile---------------------------------------------
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    contact =models.CharField(max_length=12, blank =False)
    locality = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    pincode = models.PositiveIntegerField()
    state = models.CharField(max_length = 150)


    def __str__(self):
        return str(self.first_name)

