from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),  # Register API routes under 'api/v1/'
]
