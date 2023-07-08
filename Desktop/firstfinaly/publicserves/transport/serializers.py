from rest_framework import serializers
from .models import TransportsCompany, Trips, TransportService
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TransportServesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportService
        fields = ['rating', 'date_time', 'ip_t']


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ['time', 'source', 'destination', 'Type', 'ip_tc']


class TransportsCompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportsCompany
        fields = '__all__'


class TransportsCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportsCompany
        fields = ['description', 'longitude', 'laditude', 'picture']


class TransportRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportsCompany
        fields = ('description',
                  'picture', 'site', 'rating')
        extra_kwargs = {
            'description': {'required': True},
            'site': {'required': True},
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})
    #     return attrs

    def create(self, validated_data):
        user = TransportsCompany.objects.create(
            description=validated_data['description'],
            site=validated_data['site']
        )
        # user.set_password(validated_data['password'])
        user.save()
        return user
