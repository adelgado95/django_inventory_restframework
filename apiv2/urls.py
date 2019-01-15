from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('producto/', views.ProductoViewSet.as_view({'get':'list','post':'create'})),
    path('detalle/',views.DetalleViewSet.as_view({'get':'list','post':'create'})),

]

urlpatterns = format_suffix_patterns(urlpatterns)