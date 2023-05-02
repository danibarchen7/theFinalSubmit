from django.contrib import admin
from .models import Doctors, DoctarService, Specializaion
# Register your models here.
admin.site.register(Doctors)
admin.site.register(DoctarService)
admin.site.register(Specializaion)
