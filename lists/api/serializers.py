from rest_framework import serializers
from lists.models import Lists
from items.api.serializers import ItemsSerializer


class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lists
        fields = '__all__'


class ListsDetailSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Lists
        fields = [
            'id_list', 
            'title', 
            'items'
        ]
