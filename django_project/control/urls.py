from django.urls import path

from .views import UserModelViewSet, CruiserModelViewSet, HistoryModelViewSet
from rest_framework import routers
from .views import index, login, about
# router = routers.SimpleRouter()
#
# router.register(r"users", UserModelViewSet, basename='user')
# router.register(r"cruisers", CruiserModelViewSet, basename='cruiser')
# router.register(r"histories", HistoryModelViewSet, basename='history')
# # router.register(r"accounts/login", CLoginView, basename='login')
#
# urlpatterns = router.urls

app_name = 'control'
urlpatterns = [
    path('about/', about, name='about'),
    path('', index, name='home'),
    path('login/', login, name='login'),
]