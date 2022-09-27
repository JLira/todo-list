from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.api.viewsets import UsersViewSet

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
