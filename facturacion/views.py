from django.shortcuts import render
from .models import Producto,Detalle_Factura,Factura
import os
from datetime import datetime
# Create your views here.
def index(request):
    #output = os.popen('awk -F: \'{print $1}\' /etc/passwd').read()
    output = 'Soy el index html'
    return render(request, 'index.html', {'output': output})

from django.views import generic
class ProductoListView(generic.ListView):
    model = Producto

from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['description','precio']

class FacturaListView(generic.ListView):
    model = Factura
    fields = '__all__'
    paginate_by = 10
def factura_add(request):
    new = Factura(fecha=datetime.now,total=0)
    new.save()
    productos = Producto.objects.all()
    return render(
        request,
        'facturacion/factura_add.html',
        context={'no_factura':new.id,'productos':productos},
    )
class FacturaDetailView(generic.DetailView):
    model = Factura
