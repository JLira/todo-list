from rest_framework import serializers
from users.models import Users
from lists.api.serializers import ListsDetailSerializer

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
    lists = ListsDetailSerializer(many=True, read_only=True)  
    class Meta:
        model = Users
        fields = [
            'id_user',  
            'name',     
            'email',    
            'login',    
            'password',
            'lists'
        ]