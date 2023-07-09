from rest_framework import serializers
from pharmacy.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    ip_ph = serializers.PrimaryKeyRelatedField(
        many=True, queryset=PharmaciesServies.objects.all())

    class Meta:
        model = Pharmacies
        fields = ['id', 'ip_ph']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyReview
        fields = '__all__'
class PharmacyRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacies
        fields = ('duration','pharmacy',
                  'holiday', 'night_shift', 'picture', 'pharmacy_name','longitude','laditude')
        extra_kwargs = {
            'pharmacy': {'required': True},
            'holiday': {'required': True},
            'night_shift': {'required': True},
            'pharmacy_name': {'required': True},
            'longitude': {'required': True},
            'laditude': {'required': True},
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})
    #     return attrs

    def create(self, validated_data):
        user = Pharmacies.objects.create(
            pharmacy=validated_data['pharmacy'],
            duration=validated_data['duration'],
            night_shift=validated_data['night_shift'],
            pharmacy_name=validated_data['pharmacy_name'],
            longitude=validated_data['longitude'],
            laditude=validated_data['laditude']
        )
        # user.set_password(validated_data['password'])
        user.save()
        return user


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacies
        # if i want to spcifay a fields it's look like that
        # fields = ['the fildname','the other one',and so on]
        fields = '__all__'


class MedicenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = ['medicine']