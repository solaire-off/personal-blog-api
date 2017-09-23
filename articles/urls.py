from django.conf.urls import url,include
from rest_framework import routers
from .views import PostViewSet, TagViewSet

# Router for API view
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
