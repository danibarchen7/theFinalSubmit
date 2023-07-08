from django.contrib import admin
from .models import TransportsCompany, TransportService, Trips
# Register your models here.
admin.site.register(Trips)
admin.site.register(TransportsCompany)
admin.site.register(TransportService)
