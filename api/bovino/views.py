from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from bovino.serializers import UserSerializer, GroupSerializer, BrandSerializer, BovineSerializer
from bovino.models import Brand, Bovine
from bovino.pagination import StandardResultsSetPagination


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BovineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Bovine.objects.all()
    serializer_class = BovineSerializer
    pagination_class = StandardResultsSetPagination


