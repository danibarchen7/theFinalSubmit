from django.contrib import admin
from .models import Hospitals, HospitalService, HospitalType, Competence
# Register your models here.
admin.site.register(HospitalService)
admin.site.register(Hospitals)
admin.site.register(HospitalType)
admin.site.register(Competence)
