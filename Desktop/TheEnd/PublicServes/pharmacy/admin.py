from django.contrib import admin
from .models import PharmacieServies, Pharmacies, PharmaciesContent, Medicine
# Register your models here.
admin.site.register(PharmacieServies)
admin.site.register(Pharmacies)
admin.site.register(PharmaciesContent)
admin.site.register(Medicine)
