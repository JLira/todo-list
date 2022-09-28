from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from lists.models import Lists
from lists.api.serializers import ListsSerializer
from lists.api.serializers import ListsDetailSerializer

class ListsViewSet(viewsets.ModelViewSet):
    queryset = Lists.objects.all().order_by('title')
    serializer_class = ListsSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Lists.objects.filter(pk=pk)
        self.serializer_class = ListsDetailSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)