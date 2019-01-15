from facturacion.models import Producto, Detalle_Factura
from rest_framework import viewsets
from apiv2.serializers import ProductoSerializer,DetalleSerializer
import logging

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data,list):
                kwargs["many"] = True
        logger = logging.getLogger(__name__)
        logger.error(args)

        return super(ProductoViewSet,self).get_serializer(*args,**kwargs)
class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Factura.objects.all()
    serializer_class = DetalleSerializer
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data,list):
                kwargs["many"] = True
        logger = logging.getLogger(__name__)
        logger.error(kwargs)
        return super(DetalleViewSet,self).get_serializer(*args,**kwargs)
