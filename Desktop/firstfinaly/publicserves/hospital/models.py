from django.db import models

from django.utils import timezone
from django.utils.text import slugify
from myprofile.models import Hospitals


class HospitalService(models.Model):
    ip_h = models.ForeignKey(
        Hospitals,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)

    def __str__(self):
        return self.ip_h + " " + self.rating



