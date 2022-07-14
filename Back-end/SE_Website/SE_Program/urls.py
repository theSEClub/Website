from rest_framework_nested import routers

from .Models.SE_Program import IntershipInfoViewSet
from .Models.SE_Program import COOPInfoViewSet
from .Models.SE_Program import MinorsInfoViewSet

router = routers.DefaultRouter()
router.register(r'Intership Information', IntershipInfoViewSet)
router.register(r'COOP Information', COOPInfoViewSet)
router.register(r'Minors Information', MinorsInfoViewSet)


urlpatterns = router.urls