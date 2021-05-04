from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bovino.models import Brand, Bovine


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand', 'owner']

class BovineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bovine
        fields = ['id', 'name', 'weight', 'date_birth', 'image', 'brand']