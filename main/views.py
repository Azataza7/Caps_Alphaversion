from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import Item, Brand
from .serializers import ItemSerializer, ItemValidateSerializer
from rest_framework.decorators import APIView
from django.shortcuts import Http404


class ItemApiView(APIView):
    def get(self, request):
        brand = self.request.query_params.get('brand')
        if brand:
            queryset = Item.objects.filter(brand__name=brand)
        else:
            queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateItemView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemValidateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
