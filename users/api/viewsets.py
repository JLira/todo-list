from rest_framework import viewsets
from users.api.serializers import UsersSerializer
from users.models import Users


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
