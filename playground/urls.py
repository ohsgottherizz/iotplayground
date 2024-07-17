from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, login_user, ChildViewSet, ReservationViewSet, PlaygroundOccupancyViewSet

router = DefaultRouter()
router.register(r'children', ChildViewSet, basename='child')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'occupancy', PlaygroundOccupancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]