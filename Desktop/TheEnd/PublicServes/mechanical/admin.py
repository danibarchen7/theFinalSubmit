from django.contrib import admin
from .models import Mechanical, MechanicService, TypeWork, MechanicalWork, TypeVechale
# Register your models here.
admin.site.register(Mechanical)
admin.site.register(MechanicalWork)
admin.site.register(TypeVechale)
admin.site.register(TypeWork)
admin.site.register(MechanicService)
