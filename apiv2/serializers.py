from facturacion.models import Producto, Detalle_Factura
from rest_framework import serializers

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','description','precio','stock')
    """def create(self, request, pk=None,producto=None,factura=None):
        is_many = True if isinstance(request.data,list) else False
        serializer = self.self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED, headers=headers)"""
class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Factura
        fields = ('producto','factura','cantidad','precio','subtotal')

