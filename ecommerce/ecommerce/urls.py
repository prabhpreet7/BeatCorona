from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.models import User
from store.models import Product
from rest_framework import routers
from store.views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(r'', include(router.urls)),
#     path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
#
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path(r'api/', include(router.urls)),
    # path(r'/', include('rest_framework.urls', namespace='rest_framework'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
