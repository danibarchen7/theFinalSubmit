from django.db import models

# Create your models here.


class Customer (models.Model):
    ip_c = models.IntegerField(null=False, primary_key=True)
    f_name = models.CharField(max_length=50, null=False)
    m_name = models.CharField(max_length=50, null=False)
    l_name = models.CharField(max_length=50, null=False)
    phone = models.BigIntegerField(null=False)
    password = models.CharField(max_length=50, null=False)
    e_mail = models.EmailField(max)

    def __str__(self):
        return Customer.ip_c + Customer.f_name + Customer.m_name + Customer.l_name + Customer.phone + Customer.e_mail


class DoctarService(models.Model):
    ip_c = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE
    )
    date_time = models.DateTimeField(null=False)
    ip_d = models.ForeignKey(
        "Doctors",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)
    review = models.CharField(max_length=50, null=False)


class Doctors(models.Model):
    ip_d = models.IntegerField(null=False, primary_key=True)
    f_name = models.CharField(max_length=50, null=False)
    m_name = models.CharField(max_length=50, null=False)
    l_name = models.CharField(max_length=50, null=False)
    phone = models.IntegerField(null=False)
    ip_s = models.ForeignKey(
        "Specializaion",
        on_delete=models.CASCADE
    )
    comments = models.CharField(max_length=2500, null=True)
    work_time = models.DateTimeField(null=False)
    rating = models.IntegerField(null=False)
    holiday = models.CharField(max_length=50, null=False)
    site = models.CharField(max_length=70, null=False)
    picture = models.ImageField(null=True)
    password = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.f_name + " " + self.l_name


class Specializaion(models.Model):
    ip_s = models.IntegerField(null=False, primary_key=True)
    specialization = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.specialization
