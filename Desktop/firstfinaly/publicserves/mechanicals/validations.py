from django.core.exceptions import ValidationError
from mechanicals.models import Mechanical


def custom_validation(data):
    name_m = data['name_m'].strip()
    phone = data['phone'].strip()
    password = data['password'].strip()
    ##
    if not phone or Mechanical.objects.filter(phone=phone).exists():
        raise ValidationError('choose another phone')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not name_m:
        raise ValidationError('choose another username')
    return data


def validate_email(data):
    name_m = data['name_m'].strip()
    if not name_m:
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
