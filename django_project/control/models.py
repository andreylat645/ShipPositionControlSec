from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Cruiser(models.Model):
    created = models.DateTimeField(default=timezone.now, null=True)
    title = models.CharField(max_length=60, null=True, blank=False)
    owner = models.ForeignKey('User', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Плавательные суда"

    def __str__(self):
        return self.title


class User(AbstractUser):
    roleId = models.CharField(max_length=100)
    login = models.TextField(null=True, blank=True)
    displayName = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.displayName)


class History(models.Model):
    created = models.DateTimeField(default=timezone.now, null=True)
    createdLocation = models.DateTimeField(auto_now_add=True, db_index=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    cruiser = models.ForeignKey('Cruiser', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cruiser)