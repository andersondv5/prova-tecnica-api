from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, DisciplineViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'disciplines', DisciplineViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
