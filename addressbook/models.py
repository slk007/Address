from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return self.name
    