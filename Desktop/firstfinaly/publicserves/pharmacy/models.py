from django.db import models
from myprofile.models import MyProfile,Pharmacies
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


class PharmaciesServies(models.Model):

    ip_ph = models.ForeignKey(
        Pharmacies,
        models.CASCADE,
        related_name='pharmacies'
    )
    rating = models.CharField(null=False, max_length=1)




class PharmaciesContents (models.Model):
    ip_ph = models.ForeignKey(
        Pharmacies,
        models.CASCADE
    )
    ip_pm = models.ForeignKey(
        "Medicines",
        models.CASCADE
    )
    alternative = models.CharField(max_length=150)

    def __str__(self):
        return self.alternative


class Medicines (models.Model):
    ip_m = models.IntegerField(
        null=False, primary_key=True, unique=True, auto_created=True)
    medicine = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.medicine


class PharmacyReview(models.Model):
    author = models.ForeignKey(
        MyProfile, related_name='review_author', on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(
        Pharmacies, related_name='pharmacy_review', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    # created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.pharmacy)
