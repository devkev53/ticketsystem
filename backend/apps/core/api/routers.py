from rest_framework.routers import DefaultRouter

from apps.users.api.views.user_view import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls