from rest_framework_nested import routers
from .Models.socialMedia import SocialMediaViewSet

router = routers.DefaultRouter()
router.register('socialMedia', viewset=SocialMediaViewSet)
urlpatterns = router.urls
