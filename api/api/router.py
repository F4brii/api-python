from rest_framework import routers
from bovino import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'bovines', views.BovineViewSet)