from django.contrib import admin
from .models import Mechanical, MechanicalWork, MechanicService, TypeVechale, TypeWork
# Register your models here.
admin.site.register(Mechanical)
admin.site.register(MechanicalWork)
admin.site.register(MechanicService)
admin.site.register(TypeVechale)
admin.site.register(TypeWork)
