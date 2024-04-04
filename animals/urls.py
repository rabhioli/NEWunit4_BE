from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pets.views import TagViewSet, TaskViewSet


router=routers.DefaultRouter()
router.register(r'pets', TagViewSet, TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]