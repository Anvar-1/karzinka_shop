from rest_framework import serializers
from .models import ProductModel, CategoryModel

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()

    class Meta:
        model = ProductModel
        fields = '__all__'
        # exclude = ('category',) ### category maydonini qushilmidi ####