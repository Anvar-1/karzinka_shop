from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import ProductModelSerializer
from products.models import ProductModel
from rest_framework import status

class ProductModelView(APIView):
    def get(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response({'error': "Ma'lumotlar to'liq kiritilmadi"})


class MainView(APIView):
    def get_object(self, pk):
        try:
            return ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            raise Http404("Mahsulot topilmadi")

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = ProductModelSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):  ### majbur hamma maydoni uzgartirish ###
        object = self.get_object(pk)
        serializer = ProductModelSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):  ### qaysidir maydoni uzgartirish ###
        object = self.get_object(pk)
        serializer = ProductModelSerializer(object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MainApiView(APIView):
    def get(self, request):
        return Response({'ok': 'yahshi mahsulot'})