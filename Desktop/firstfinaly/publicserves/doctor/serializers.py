from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from myprofile.models import Doctors

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ('ip_s','doctor',
                  'description', 'holiday', 'picture', 'longitude','laditude')
        extra_kwargs = {
            'ip_s': {'required': True},
            'doctor': {'required': True},
            'holiday': {'required': True},
            'longitude': {'required': True},
            'laditude': {'required': True},
            'description': {'required': True},
        }

    def create(self, validated_data):
        user = Doctors.objects.create(
            ip_s=validated_data['ip_s'],
            doctor=validated_data['doctor'],
            holiday=validated_data['holiday'],
            description=validated_data['description'],
            longitude=validated_data['longitude'],
            laditude=validated_data['laditude']
        )

    #     # user.set_password(validated_data['password'])
        user.save()
        return user


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorReview
        fields = '__all__'
