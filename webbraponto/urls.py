from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from employees.api import viewsets as employeesviewsets

route = routers.DefaultRouter()

route.register(r'employees', employeesviewsets.EmployeesViewSet, basename="Employees")

from webbraponto.home_view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
