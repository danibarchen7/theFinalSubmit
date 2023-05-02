from django.contrib import admin
from .models import TransportsCompany, TransportService, TransportType, Trips
# Register your models here.
admin.site.register(TransportsCompany)
admin.site.register(TransportService)
admin.site.register(TransportType)
admin.site.register(Trips)
