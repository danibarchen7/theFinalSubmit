from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer (models.Model):
    ip_c = models.IntegerField(null=False, primary_key=True)
    customer = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, null=False)

    def __str__(self):
        return self.customer.first_name
