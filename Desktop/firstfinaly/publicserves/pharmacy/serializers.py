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


class PharmacyRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacies
        fields = ('duration',
                  'holiday', 'night_shift', 'picture', 'site')
        extra_kwargs = {
            'holiday': {'required': True},
            'night_shift': {'required': True},
            'site': {'required': True},
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})
    #     return attrs

    def create(self, validated_data):
        user = Pharmacies.objects.create(
            duration=validated_data['duration'],
            night_shift=validated_data['night_shift'],
            site=validated_data['site']
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
