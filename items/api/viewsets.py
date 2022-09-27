from rest_framework import viewsets
from rest_framework.decorators import action
from items.api.serializers import ItemsDetailsSerializer, ItemsSerializer
from items.models import Items
from rest_framework.response import Response

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('title')
    serializer_class = ItemsSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Items.objects.filter(pk=pk)
        self.get_serializer_class = ItemsDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)