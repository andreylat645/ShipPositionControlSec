from .views import UserModelViewSet, CruiserModelViewSet, HistoryModelViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"users", UserModelViewSet, basename='user')
router.register(r"cruisers", CruiserModelViewSet, basename='cruiser')
router.register(r"histories", HistoryModelViewSet, basename='history')

urlpatterns = router.urls
