from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Users
from users.api.serializers import UsersSerializer
from users.api.serializers import UserDetailsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Users.objects.filter(pk=pk)
        self.serializer_class = UserDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

