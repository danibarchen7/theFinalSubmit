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


class TransportService(models.Model):
    ip_c = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE
    )
    date_time = models.DateTimeField(null=False)
    ip_t = models.ForeignKey(
        "Trips",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(null=False)
    review = models.CharField(max_length=2500, null=False)


class Trips (models.Model):
    ip_t = models.IntegerField(null=False, primary_key=True)
    ip_tc = models.ForeignKey(
        "TransportsCompany",
        on_delete=models.CASCADE
    )
    time = models.DateTimeField(null=False)
    phone = models.BigIntegerField(null=False)
    source = models.CharField(null=False, max_length=100)
    destination = models.CharField(null=False, max_length=100)
    ip_type = models.ForeignKey(
        "TransportType",
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.source + "-->"+self.destination


class TransportsCompany(models.Model):
    ip_tc = models.IntegerField(null=False, primary_key=True)
    name_tc = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=10, null=False)
    phone = models.BigIntegerField(null=False)
    site = models.CharField(max_length=50, null=False)
    picture = models.ImageField(null=False)
    comments = models.TextField(max_length=2500, null=False)
    rating = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.name_tc


class TransportType(models.Model):
    ip_type = models.IntegerField(null=False, primary_key=True)
    Type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.Type
