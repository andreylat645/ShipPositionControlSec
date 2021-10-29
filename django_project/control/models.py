from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import date


class Cruiser(models.Model):
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    code = models.CharField(max_length=60, null=True, blank=False,)
    title = models.CharField(max_length=60, null=True, blank=False, unique=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.title


class User(AbstractUser):
    ROLEID = (
        (None, 'None'),
        ('admin', 'Администратор'),
        ('owner', 'Владелец судна')
    )
    roleId = models.CharField(max_length=100, choices=ROLEID, null=True, blank=True)
    login = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)


class History(models.Model):
    code = models.CharField(max_length=60, null=True, blank=False)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(auto_now=False, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    cruiser = models.ForeignKey('Cruiser', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Histories"

    def __str__(self):
        return str(self.cruiser)
