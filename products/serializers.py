from rest_framework import serializers
from .models import ProductModel, CategoryModel

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    # category = CategoryModelSerializer()

    class Meta:
        model = ProductModel
        fields = '__all__'
        # exclude = ('category',) ### category maydoni qushilmidi ####

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance
