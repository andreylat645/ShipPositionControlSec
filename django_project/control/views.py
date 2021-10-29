from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.views import LoginView


from .models import *
from .serializers import UserSerializer, CruiserSerializer, HistorySerializer

menu = ['О Сайте', 'Войти']


def index(request):
    histories = History.objects.all()
    return render(request, 'control/index.html', {'histories': histories, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'control/about.html', {'title': 'О сайте'})


def login(request):
    return render(request, 'control/login.html', {'title': 'Страница входа пользователя'})


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CruiserModelViewSet(viewsets.ModelViewSet):
    serializer_class = CruiserSerializer
    queryset = Cruiser.objects.all()


class HistoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()



