from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.api.viewsets import UsersViewSet
from items.api.viewsets import ItemsViewSet
from lists.api.viewsets import ListsViewSet


# router = routers.SimpleRouter()
router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'lists', ListsViewSet)
router.register(r'items', ItemsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
