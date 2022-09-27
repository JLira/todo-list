from rest_framework import viewsets
from items.api.serializers import ItemsSerializer
from items.models import Items


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('title')
    serializer_class = ItemsSerializer
