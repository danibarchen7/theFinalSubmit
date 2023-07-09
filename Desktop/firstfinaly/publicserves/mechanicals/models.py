from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify
from myprofile.models import MyProfile,Mechanical


class MechanicService(models.Model):

    ip_m = models.ForeignKey(
        Mechanical,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=10)
    comments = models.CharField(max_length=2500, null=False)

    def __str__(self) -> str:
        return self.rating + " "+self.comments




class TypeWork(models.Model):
    ip_type = models.BigAutoField(null=False, primary_key=True,
                                  unique=True, auto_created=True)
    type = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.type


class MechanicalWork (models.Model):
    ip_m = models.ForeignKey(
        Mechanical,
        on_delete=models.CASCADE
    )
    ip_type = models.ForeignKey(
        "TypeVechale",
        on_delete=models.CASCADE
    )


class TypeVechale(models.Model):
    ip_type = models.BigAutoField(null=False, primary_key=True,
                                  unique=True, auto_created=True)
    type = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.type


class MechanicalReview(models.Model):
    author = models.ForeignKey(
        MyProfile, on_delete=models.CASCADE)
    mechanical = models.ForeignKey(
        Mechanical, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])
    # created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.mechanical)
