from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
from django.urls import reverse
import uuid


# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    description=models.CharField(max_length=200,help_text="Enter a product name")
    precio = models.DecimalField(decimal_places=2,max_digits=7,validators=[MinValueValidator(Decimal('0.01'))],)
    stock = models.IntegerField()
    #Necesaria para poder acceder
    def get_absolute_url(self):
        return reverse('productos')

class Factura (models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True)
    total = models.DecimalField(decimal_places=2,max_digits=7)
    def get_absolute_url(self):
        return reverse('facturas')


class Detalle_Factura (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text="ID unico para esta factura")
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    factura = models.ForeignKey('Factura', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=7)
    subtotal = models.DecimalField(decimal_places=2, max_digits=7)
