from rest_framework import serializers
from .models import Mechanical, TypeWork,MechanicalReview,TypeVechale
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TypeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeWork
        fields = '__all'

class TypeVichaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeVechale
        fields = '__all__'


class MechanicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanical
        fields = '__all__'


class MechanicalRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanical
        fields = ('ip_type',
                  'holiday', 'picture', 'longitude','laditude','mechanical_name')
        extra_kwargs = {
            'ip_type': {'required': True},
            'holiday': {'required': True},
            'longitude': {'required': True},
            'laditude': {'required': True},
            'mechanical_name': {'required': True},
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})
    #     return attrs

    def create(self, validated_data):
        user = Mechanical.objects.create(
            ip_tupe=validated_data['ip_type'],
            holiday=validated_data['holiday'],
            longitude=validated_data['longitude'],
            laditude=validated_data['laditude'],
            mechanical_name=validated_data['mechanical_name'],

        )

        # user.set_password(validated_data['password'])
        user.save()
        return user
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MechanicalReview
        fields = '__all__'