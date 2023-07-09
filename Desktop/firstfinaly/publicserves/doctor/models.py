from django.db import models
from django.utils.text import slugify
# Create your models here.
from myprofile.models import Doctors,MyProfile


class DoctarService(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    ip_d = models.ForeignKey(
        Doctors,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)


class DoctorReview(models.Model):
    author = models.ForeignKey(
        MyProfile, on_delete=models.CASCADE)
    hospital = models.ForeignKey(
        Doctors, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])
    # created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.hospital)