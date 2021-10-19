from rest_framework import serializers
from .models import User, Cruiser, History


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("roleId", "first_name", "last_name", "username")


class CruiserSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(slug_field="username", read_only=True, many=True)

    class Meta:
        model = Cruiser
        fields = ("created", "code", "title", "owner")


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("created", "createdLocation", "longitude", "latitude", "cruiser")


