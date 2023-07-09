from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TransportServesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportService
        fields = ['rating', 'date_time', 'ip_t']


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ['time', 'source', 'destination', 'Type', 'ip_tc','ip_t']


class TransportsCompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportsCompany
        fields = '__all__'


class TransportsCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportsCompany
        fields = ['company_name','description', 'longitude', 'laditude', 'picture','transport']


class TransportRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportsCompany
        fields = ('description','transport',
                  'picture', 'laditude','longitude', 'company_name')
        extra_kwargs = {
            'transport': {'required': True},
            'description': {'required': True},
            'longitude': {'required': True},
            'laditude': {'required': True},
            'company_name': {'required': True},
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})
    #     return attrs

    def create(self, validated_data):
        user = TransportsCompany.objects.create(
            transport=validated_data['transport'],
            description=validated_data['description'],
            longitude=validated_data['longitude'],
            laditude=validated_data['laditude'],
            company_name=validated_data['company_name']
        )
        # user.set_password(validated_data['password'])
        user.save()
        return user

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCompanyReview
        fields = '__all__'
