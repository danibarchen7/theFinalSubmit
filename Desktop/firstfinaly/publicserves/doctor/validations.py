from django.core.exceptions import ValidationError
from doctor.models import Doctors, Specializaion


def custom_validation(data):
    fullname = data['fullname'].strip()
    phone = data['phone'].strip()
    password = data['password'].strip()
    ##
    if not phone or Doctors.objects.filter(phone=phone).exists():
        raise ValidationError('choose another phone')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not fullname:
        raise ValidationError('choose another username')
    return data


def validate_email(data):
    fullname = data['fullname'].strip()
    if not fullname:
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
