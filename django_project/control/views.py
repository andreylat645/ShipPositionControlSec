
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, Cruiser, History
from .serializers import UserSerializer, CruiserSerializer, HistorySerializer


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CruiserModelViewSet(viewsets.ModelViewSet):
    serializer_class = CruiserSerializer
    queryset = Cruiser.objects.all()


class HistoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()

