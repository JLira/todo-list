from rest_framework import serializers
from items.models import Items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class ItemsDetailsSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Items
        fields = [
             'id_item',
             'title',
             'description',
             'id_list'
        ]