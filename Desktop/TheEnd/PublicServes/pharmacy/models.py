from django.db import models
from customer.models import Customer

# Create your models here.


class PharmacieServies(models.Model):
    FRIDAY = "FR"
    SUNDAY = "SU"
    MANDAY = "MA"
    TUSEDAY = "TU"
    WEDNESDAY = "WE"
    THERSDAY = "TH"
    DAYS_CHOICES = [
        (FRIDAY, "Friday"),
        (SUNDAY, "Sunday"),
        (MANDAY, "Manday"),
        (TUSEDAY, "Tuseday"),
        (WEDNESDAY, "Wednesday"),
        (THERSDAY, "Thersday"),
    ]
    ip_c = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    date_time = models.CharField(
        max_length=2,
        choices=DAYS_CHOICES,
        default="FR",
    )
    ip_ph = models.ForeignKey(
        "Pharmacies",
        models.CASCADE
    )
    rating = models.IntegerField(null=False)


class Pharmacies (models.Model):
    # the days that he works
    FRIDAY = "FR"
    SUNDAY = "SU"
    MANDAY = "MA"
    TUSEDAY = "TU"
    WEDNESDAY = "WE"
    THERSDAY = "TH"
    DAYS_CHOICES = [
        (FRIDAY, "Friday"),
        (SUNDAY, "Sunday"),
        (MANDAY, "Manday"),
        (TUSEDAY, "Tuseday"),
        (WEDNESDAY, "Wednesday"),
        (THERSDAY, "Thersday"),
    ]
    ip_ph = models.IntegerField(null=False, primary_key=True)
    name_ph = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=13, null=False)
    duration = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    holiday = models.CharField(
        max_length=2,
        choices=DAYS_CHOICES,
        default="FR",

    )
    night_shift = models.DateField(auto_now=False, auto_now_add=False)
    picture = models.ImageField(
        null=True, upload_to="static\PublicServes\images")
    site = models.CharField(max_length=50)
    rate = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name_ph


class PharmaciesContent (models.Model):
    ip_ph = models.ForeignKey(
        "Pharmacies",
        models.CASCADE
    )
    ip_pm = models.ForeignKey(
        "Medicine",
        models.CASCADE
    )
    alternative = models.BooleanField()

    def __str__(self):
        return self.alternative


class Medicine (models.Model):
    ip_m = models.IntegerField(null=False, primary_key=True)
    medicine = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.medicine
