from facturacion.models import Producto
# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from apiapp.serializers import ProductoSerializer

class ProductoListApi(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
