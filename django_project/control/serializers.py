from rest_framework import serializers
from .models import User, Cruiser, History


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("roleId", "login", "displayName")


class CruiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cruiser
        fields = ("created", "title", "owner")


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("created", "createdLocation", "longitude", "latitude", "cruiser")


