from django.db import models
from customer.models import Customer
from django.utils import timezone
# Create your models here.

# how to import app in another  django app?


class DoctarService(models.Model):
    ip_c = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    date_time = models.DateTimeField(default=timezone.now)
    ip_d = models.ForeignKey(
        "Doctors",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)


class Doctors(models.Model):
    ip_d = models.IntegerField(null=False, primary_key=True)
    fullname = models.TextField(max_length=55)
    phone = models.CharField(max_length=13, null=False)
    ip_s = models.ForeignKey(
        "Specializaion",
        on_delete=models.CASCADE
    )
    comments = models.CharField(max_length=2500, null=True)
    rating = models.IntegerField(null=False)
    holiday = models.CharField(max_length=50, null=False)
    site = models.CharField(max_length=70, null=False)
    picture = models.ImageField(null=True)
    password = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.f_name + " " + self.l_name


class Specializaion(models.Model):
    ip_s = models.IntegerField(null=False, primary_key=True)
    specialization = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.specialization
