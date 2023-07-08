from django.core.exceptions import ValidationError
from .models import Hospitals


def custom_validation(data):
    name_h = data['name_h'].strip()
    phone = data['phone'].strip()
    password = data['password'].strip()
    ##
    if not phone or Hospitals.objects.filter(email=phone).exists():
        raise ValidationError('choose another phone')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not name_h:
        raise ValidationError('choose another username')
    return data


def validate_email(data):
    name_ph = data['name_h'].strip()
    if not name_ph:
        raise ValidationError('an name pharmacy is needed')
    return True


def validate_username(data):
    phone = data['phone'].strip()
    if not phone:
        raise ValidationError('choose another username')
    return True


def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True
