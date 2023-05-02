from rest_framework.serializers import ModelSerializer
from .models import Pharmacies


class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacies
        # if i want to spcifay a fields it's look like that
        # fields = ['the fildname','the other one',and so on]
        fields = '__all__'
