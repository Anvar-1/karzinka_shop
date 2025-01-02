from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import ProductModelSerializer
from products.models import ProductModel

class ProductModelView(APIView):

    def get(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductModelSerializer(queryset, many=True)
        return Response(serializer.data)


class MainApiView(APIView):

    def get(self, request):
        return Response({'ok': 'yahshi mahsulot'})