from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
emprouter = DefaultRouter()
emprouter.register(r'emp', EmployeeViewSet)

urlpatterns = [
    path('router/', include(emprouter.urls)),
]