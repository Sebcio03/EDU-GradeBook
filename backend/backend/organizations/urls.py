from rest_framework.routers import DefaultRouter

from backend.organizations.views import OrganizationViewSet

router = DefaultRouter()
router.register('', OrganizationViewSet, basename='organization')

urlpatterns = [
    
] + router.urls