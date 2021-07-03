from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pasteleria.models import Cliente, Producto

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    
        fields = ['url', 'rut', 'nombre']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url', 'nombre_producto', 'precio']