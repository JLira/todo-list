from rest_framework import viewsets
from lists.api.serializers import ListsSerializer,ListsDetailSerializer
from lists.models import Lists
from rest_framework.response import Response

class ListsViewSet(viewsets.ModelViewSet):
    queryset = Lists.objects.all().order_by('title')
    serializer_class = ListsSerializer


    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Lists.objects.filter(pk=pk)
        self.serializer_class = ListsDetailSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)