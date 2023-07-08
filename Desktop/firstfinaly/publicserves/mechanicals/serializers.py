from rest_framework import serializers
from .models import Mechanical, TypeWork
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TypeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeWork
        fields = '__all'


class MechanicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanical
        fields = '__all__'


class MechanicalRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanical
        fields = ('ip_type',
                  'holiday', 'picture', 'site')
        extra_kwargs = {
            'ip_type': {'required': True},
            'holiday': {'required': True},
            'site': {'required': True},
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
            site=validated_data['site'],

        )

        # user.set_password(validated_data['password'])
        user.save()
        return user
