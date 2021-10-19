from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Cruiser(models.Model):
    created = models.DateTimeField(default=timezone.now, null=True)
    code = models.CharField(max_length=60, null=True, blank=False)
    title = models.CharField(max_length=60, null=True, blank=False)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    ROLEID = (
        (None, 'None'),
        ('admin', 'Администратор'),
        ('owner', 'Владелец судна')
    )
    roleId = models.CharField(max_length=100, choices=ROLEID)
    login = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)


class History(models.Model):
    created = models.DateTimeField(default=timezone.now, null=True)
    createdLocation = models.DateTimeField(auto_now_add=True, db_index=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    cruiser = models.ForeignKey('Cruiser', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cruiser)