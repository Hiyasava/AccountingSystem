from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    position = models.CharField(max_length=128, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    bank_card = models.IntegerField(blank=True, null=True)
    pay_form = models.CharField(max_length=128, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)