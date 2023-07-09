from django.db import models

from django.utils import timezone
from django.utils.text import slugify
from myprofile.models import Hospitals ,MyProfile


class HospitalService(models.Model):
    ip_h = models.ForeignKey(
        Hospitals,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)

    def __str__(self):
        return self.ip_h + " " + self.rating



class HospitalReview(models.Model):
    author = models.ForeignKey(
        MyProfile, on_delete=models.CASCADE)
    hospital = models.ForeignKey(
        Hospitals, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])
    # created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.hospital)