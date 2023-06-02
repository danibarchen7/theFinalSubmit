from rest_framework.serializers import ModelSerializer
from pharmacy.models import Pharmacies
from doctor.models import Doctors


class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacies
        # if i want to spcifay a fields it's look like that
        # fields = ['the fildname','the other one',and so on]
        fields = '__all__'


class DoctorsSerializer(ModelSerializer):
    class Meta:
        model = Doctors

        fields = '__all__'
