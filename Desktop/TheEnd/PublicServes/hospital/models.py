from django.db import models

# Create your models here.


class HospitalService(models.Model):
    ip_c = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE
    )
    date_time = models.DateField(null=False)
    ip_h = models.ForeignKey(
        "Hospitals",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)
    review = models.CharField(null=True, max_length=50)


class Hospitals (models.Model):
    ip_h = models.IntegerField(null=False, primary_key=True)
    name_h = models.CharField(null=False, max_length=50)
    phone = models.models.BigIntegerField(null=False)
    ip_t = models.ForeignKey(
        "HospitalType",
        on_delete=models.CASCADE
    )
    ip_c = models.ForeignKey(
        "Competence",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)
    comments = models.CharField(max_length=50, null=False)
    picture = models.ImageField(null=False)
    site = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.name_h


class HospitalType (models.Model):
    ip_type = models.IntegerField(null=False, primary_key=True)
    Type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.Type


class Competence (models.Model):
    ip_competence = models.IntegerField(null=False, primary_key=True)
    competence = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.competence
