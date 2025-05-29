from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CandidatViewSet, RecruteurViewSet, CandidatureViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'candidats', CandidatViewSet)
router.register(r'recruteurs', RecruteurViewSet)
router.register(r'candidatures', CandidatureViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
