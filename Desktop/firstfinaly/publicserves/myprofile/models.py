from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.text import slugify
# Create your models here.



class Mechanical(models.Model):
    MECHANICAL = "ME"
    ELCTRONICAL = "EL"
    KOMAJE = "KO"
    SOAAJE = "SO"
    WORKTYPE_CHOICES = [
        (MECHANICAL,"Mechanical"),
        (ELCTRONICAL,"Elctronical"),
        (KOMAJE,"Komaje"),
        (SOAAJE,"Soaaje"),
        
    ]
    ip_m = models.BigAutoField(null=False, primary_key=True,
                               unique=True, auto_created=True)
    mechanical = models.ForeignKey("MyProfile", on_delete=models.CASCADE)
    ip_type = models.CharField(
        max_length=2,
        choices=WORKTYPE_CHOICES,
        default="ME",

    )
    holiday = models.CharField(max_length=50, null=True)
    picture = models.ImageField(
        null=True, blank=True, upload_to="static\PublicServes\images")
    longitude = models.FloatField(null=True)
    laditude = models.FloatField(null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.mechanical)

        # Call the real save() method
        super(Mechanical, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.mechanical)

class TransportsCompany(models.Model):
    ip_tc = models.BigAutoField(null=False, primary_key=True,
                                unique=True, auto_created=True)
    transport = models.ForeignKey("MyProfile", on_delete=models.CASCADE)
    longitude = models.FloatField(null=True)
    laditude = models.FloatField(null=True)
    picture = models.ImageField(null=True, upload_to="media")
    description = models.TextField(max_length=2500, null=True)

    def __str__(self) -> str:
        return self.transport


class Pharmacies (models.Model):
    # the days that he works
    FRIDAY = "FR"
    SUNDAY = "SU"
    MANDAY = "MA"
    TUSEDAY = "TU"
    WEDNESDAY = "WE"
    THERSDAY = "TH"
    DAYS_CHOICES = [
        (FRIDAY, "Friday"),
        (SUNDAY, "Sunday"),
        (MANDAY, "Manday"),
        (TUSEDAY, "Tuseday"),
        (WEDNESDAY, "Wednesday"),
        (THERSDAY, "Thersday"),
    ]
    id = models.BigAutoField(null=False, primary_key=True,
                             unique=True, auto_created=True)
    pharmacy = models.ForeignKey("MyProfile", on_delete=models.CASCADE)
    duration = models.CharField(max_length=50, null=True)
    holiday = models.CharField(
        max_length=2,
        choices=DAYS_CHOICES,
        default="FR",

    )
    night_shift = models.BooleanField(default=False)
    picture = models.ImageField(
        null=True, upload_to="static\PublicServes\images")
    longitude = models.FloatField( null=True)
    laditude = models.FloatField( null=True)
    # created_at = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pharmacy)

        # Call the real save() method
        super(Pharmacies, self).save(*args, **kwargs)

    def __str__(self):
        return self.pharmacy + " and the holiday " + self.holiday


class Hospitals (models.Model):
    GOVERMENT = "GO"
    PRIVATE = "PR"

    HOSPITALS_CHOICES = [
        (GOVERMENT, "Goverment"),
        (PRIVATE, "Private"),

    ]
    ip_h = models.BigAutoField(null=False, primary_key=True,
                               unique=True, auto_created=True)

    ip_t = models.CharField(
        max_length=2,
        choices=HOSPITALS_CHOICES,
        default="GO",

    )
    CANCERANDRADIOTHERAPY = "CART"
    CHILDREN = "CHILDREN"
    HARTANDBODY = "HAAB"
    SICOANDBRANI = "SIAB"
    BRAINANDNARROW = "BRAN"
    ALLSPECIALIEST = "ALSP"
    HOSPITALS_SPECIALIZATION_CHOICES = [
        (CANCERANDRADIOTHERAPY,"Radiotheraoy or Chemptherapy"),
        (CHILDREN,"Children hospital"),
        (HARTANDBODY,"Hart and Body hospital"),
        (SICOANDBRANI,"Mental and crazies hospital"),
        (BRAINANDNARROW,"Brain and Narrow hospital"),
        (ALLSPECIALIEST,"All Specialest hospital"),
    ]
    specialization = models.CharField(max_length=8,
                                      choices=HOSPITALS_SPECIALIZATION_CHOICES
                                      ,default="ALSP")
    hospital = models.ForeignKey("MyProfile", on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True)
    picture = models.ImageField(
        null=True, blank=True, upload_to="static\PublicServes\images")
    longitude = models.FloatField(null=True)
    laditude = models.FloatField( null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.hospital)

        # Call the real save() method
        super(Hospitals, self).save(*args, **kwargs)

    def __str__(self):
        return self.hospital


class Doctors(models.Model):
    OPHTHALMOLOGIST = "OP"
    CARDIOLOGIST = "CA"
    BONS = "BO"
    ASETHETICIAN = "AS"
    NEUROLOGIST = "NE"
    PEDIATRICIAN = "PE"
    SPECIALIZATIONS_CHOICES = [
        (OPHTHALMOLOGIST, "EYE doctor"),
        (CARDIOLOGIST, "Hart doctor"),
        (BONS, "Bons doctor"),
        (ASETHETICIAN, "Beuaty doctor"),
        (NEUROLOGIST, "Brain doctor "),
        (PEDIATRICIAN, "Children doctor"),
    ]
    id = models.BigAutoField(null=False, primary_key=True,
                             unique=True, auto_created=True)
    doctor = models.ForeignKey(
        "MyProfile", on_delete=models.CASCADE)
    ip_s = models.CharField(
        max_length=2,
        choices=SPECIALIZATIONS_CHOICES,
        default="OP",

    )
    description = models.CharField(max_length=2500, null=True, blank=True)
    holiday = models.CharField(max_length=50, null=True)
    longitude = models.FloatField(default=0.0,null=True)
    laditude = models.FloatField(default=0.0,null=True)
    picture = models.ImageField(
        null=True, blank=True, upload_to="static\PublicServes\images")
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.doctor)

        # Call the real save() method
        super(Doctors, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.doctor

class MyProfile(AbstractUser):
    DOCTOR = "DR"
    HOSPITAL = "HO"
    MECHANICAL = "ME"
    USER = "US"
    PHARMACY = "PH"
    TRANSPORT = "TR"
    USER_CHOICES = [
        (USER, "User"),
        (PHARMACY, "Pharmacy"),
        (MECHANICAL, "Mechanical"),
        (TRANSPORT, "Transport"),
        (DOCTOR, "Doctor"),
        (HOSPITAL, "Hospital"),
    ]
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=13)
    user_type = models.CharField(
        max_length=2,
        choices=USER_CHOICES,
        default="US",

    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', 'phone',)
    objects = CustomUserManager()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.email)

        # Call the real save() method
        super(MyProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
    def create_related(self):
        if self.user_type == "HO":
            hospital = Hospitals.objects.create(
                hospital=self,
                ip_t=self.user_type,
                ip_c="",
                description="",
                picture="",
                longitude=0,
                laditude=0,
            )
            hospital.save()
        elif self.user_type=="DR":
            doctor = Doctors.objects.create(
                doctor=self,
                ip_t=self.user_type,
                description = "",
                holiday = "",
                longitude = 0,
                laditude = 0,
                picture = "",
            )
            doctor.save()
        elif self.user_type=="ME":
            mechanical = Mechanical.objects.create(
                mechanical=self,
                ip_type = "",
                holiday = "",
                picture = "",
                longitude = 0,
                laditude = 0
            )
            mechanical.save()
        elif self.user_type == "PH":
            pharmacy = Pharmacies.objects.create(
                pharmacy=self,
                duration ="",
                holiday = "",
                night_shift = True,
                picture = "",
                longitude = 0,
                laditude = 0
            )
            pharmacy.save()
        else:
            transport = TransportsCompany.objects.create(
             description = "",
                picture = "",
                longitude = 0,
                laditude = 0
            )
            transport.save()
            