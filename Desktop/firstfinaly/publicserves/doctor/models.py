from django.db import models
from django.utils.text import slugify
# Create your models here.
from myprofile.models import Doctors


class DoctarService(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    ip_d = models.ForeignKey(
        Doctors,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)


