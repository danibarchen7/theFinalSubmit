from rest_framework.serializers import CharField
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers, validators
from rest_framework import serializers
from .models import MyProfile


class UserSerializer(serializers.ModelSerializer):
    # phone = serializers.CharField(max_length=16)

    class Meta:
        model = MyProfile
        fields = '__all__'


class LoginSerializer(serializers.Serializer):

    phone = CharField(max_length=255)
    password = CharField(max_length=255)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=MyProfile.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MyProfile
        fields = ('username', 'password', 'password2',
                  'email', 'phone','user_type', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'duration': {'required': False},
            'holiday': {'required': False},
            'longitude': {'required': False},
            'laditude': {'required': False},
            
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = MyProfile.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_type = validated_data['user_type']
        )
        
        user.create_related()
        user.set_password(validated_data['password'])
        user.save()
        return user
