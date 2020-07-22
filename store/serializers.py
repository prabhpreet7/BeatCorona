from rest_framework import serializers

from django.contrib.auth.models import User
from store.models import Product

# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'digital', 'info')
