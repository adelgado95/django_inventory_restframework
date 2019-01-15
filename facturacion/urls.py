from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'productos', views.ProductoListView.as_view(), name='productos'),
    url(r'producto/create', views.ProductoCreate.as_view(), name='producto-create'),
    url(r'producto/(?P<pk>\d+)/edit', views.ProductoUpdate.as_view(), name='producto-edit'),
    url(r'factura/new', views.factura_add, name='factura-new'),
    url(r'facturas', views.FacturaListView.as_view(), name='facturas'),
    url(r'factura/(?P<pk>\d+)', views.FacturaDetailView.as_view(), name='factura-detalle'),


]