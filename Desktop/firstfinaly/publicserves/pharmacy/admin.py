from django.contrib import admin
from .models import Pharmacies,PharmaciesContents,PharmaciesServies,PharmacyReview,Medicines
# Register your models here.

admin.site.register(Pharmacies)
admin.site.register(PharmaciesContents)
admin.site.register(PharmaciesServies)
admin.site.register(PharmacyReview)
admin.site.register(Medicines)