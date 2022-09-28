from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from items.models import Items
from items.api.serializers import ItemsSerializer
from items.api.serializers import ItemsDetailsSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('title')
    serializer_class = ItemsSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Items.objects.filter(pk=pk)
        self.serializer_class = ItemsDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)