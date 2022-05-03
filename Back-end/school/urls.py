from rest_framework_nested import routers

from school.views.Student import StudentViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = router.urls
