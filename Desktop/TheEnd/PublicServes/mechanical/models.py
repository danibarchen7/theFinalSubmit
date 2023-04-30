from django.db import models

# Create your models here.


class MechanicService(models.Model):
    ip_c = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE
    )
    date_time = models.DateTimeField(null=False)
    ip_m = models.ForeignKey(
        "Mechanical",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=10)
    review = models.CharField(max_length=2500, null=False)


class Mechanical(models.Model):
    ip_m = models.IntegerField(null=False, primary_key=True)
    name_m = models.CharField(max_length=50, null=False)
    phone = models.BigIntegerField(null=False)
    ip_type = models.ForeignKey(
        "TypeWork",
        on_delete=models.CASCADE
    )
    work_time = models.DateTimeField(null=False)
    holiday = models.CharField(max_length=50, null=False)
    rating = models.IntegerField(null=False)
    picture = models.ImageField(null=True)
    comments = models.CharField(max_length=2500, null=False)
    site = models.CharField(null=True)
    password = models.CharField(max_length=10, null=False)

    def __str__(self) -> str:
        return self.name_m


class TypeWork(models.Model):
    ip_type = models.IntegerField(null=False, primary_key=True)
    type = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.type


class MechanicalWork (models.Model):
    ip_m = models.ForeignKey(
        "Mechanical",
        on_delete=models.CASCADE
    )
    ip_type = models.ForeignKey(
        "TypeVechale",
        on_delete=models.CASCADE
    )


class TypeVechale(models.Model):
    ip_type = models.IntegerField(null=False, primary_key=True)
    type = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.type
