from rest_framework import serializers
from doctor.models import Doctors
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ('ip_s',
                  'description', 'holiday', 'picture', 'site', 'rate')
        extra_kwargs = {
            'ip_s': {'required': True},
            'holiday': {'required': True},
            'site': {'required': True},
            'description': {'required': True},
        }

    def create(self, validated_data):
        user = Doctors.objects.create(
            ip_s=validated_data['ip_s'],
            holiday=validated_data['holiday'],
            description=validated_data['description'],
            site=validated_data['site']
        )

    #     # user.set_password(validated_data['password'])
        user.save()
        return user


# doctor specialization serializer

    # specialization = serializers.CharField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=Specializaion.objects.all())]
    # )

    # class Meta:
    #     model = Specializaion
    #     fields = '__all__'
    #     extra_kwargs = {
    #         ' specialization': {'required': True}
    #     }

    # def create(self, validated_data):
    #     user = Specializaion.objects.create(
    #         specialization=validated_data['specialization']
    #     )

    #     # user.set_password(validated_data['password'])
    #     user.save()
    #     return user
