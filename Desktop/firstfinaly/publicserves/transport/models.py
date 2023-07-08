from django.db import models
# Create your models here.
from myprofile.models import TransportsCompany


class TransportService(models.Model):

    ip_t = models.ForeignKey(
        "Trips",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)


class Trips (models.Model):
    VIP = "VI"
    NORMAL = "NO"

    TRIPS_CHOICES = [
        (VIP, "Vip"),
        (NORMAL, "Normal"),

    ]
    ip_t = models.BigAutoField(
        null=False, primary_key=True, unique=True, auto_created=True)
    ip_tc = models.ForeignKey(
        TransportsCompany,
        on_delete=models.CASCADE
    )
    time = models.DateTimeField(null=False)
    source = models.CharField(null=False, max_length=100)
    destination = models.CharField(null=False, max_length=100)
    Type = models.CharField(
        max_length=2,
        choices=TRIPS_CHOICES,
        default="NO",

    )

    def __str__(self) -> str:
        return Trips.source + " to "+Trips.destination + " and the time: "+Trips.time

    # def __str__(self) -> str:
    #     return self.source + "-->"+self.destination




class TransportType(models.Model):
    ip_type = models.BigAutoField(
        null=False, primary_key=True, auto_created=True, unique=True)
    Type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.Type
