from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tekken.views import TekkenViewSet

router = routers.DefaultRouter()
router.register('tekken', TekkenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
