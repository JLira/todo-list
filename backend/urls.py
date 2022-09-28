from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


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
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/', include(router.urls)),
]
