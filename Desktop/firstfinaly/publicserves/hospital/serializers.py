from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from .models import *

class HospitalServecSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalService
        fields = '__all__'


class HospitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields = '__all__'


class HospitalRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields = ('ip_t', 'specialization',
                  'description', 'picture', 'longitude','laditude','hospital','hospital_name')
        extra_kwargs = {
            'longitude': {'required': True},
            'laditude': {'required': True},
            'ip_t': {'required': True},
            'specialization': {'required': True},
            'hospital': {'required': True},
            'hospital_name': {'required': True},
        }

    # def create_type(self, validated_data):
    #     user = HospitalType.objects.create(
    #         Type=validated_data['Type']
    #     )
    #     user.save()
    #     return user

    def create(self, validated_data):
        user = Hospitals.objects.create(
            ip_t=validated_data['ip_t'],
            specialization=validated_data['specialization'],
            longitude=validated_data['longitude'],
            laditude=validated_data['laditude'],
            hospital=validated_data['hospital'],
            hospital_name=validated_data['hospital_name']

        )
        # user.set_password(validated_data['password'])
        user.save()
        return user
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalReview
        fields = '__all__'