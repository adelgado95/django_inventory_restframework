# Generated by Django 2.1.5 on 2019-01-10 20:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Factura',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID unico para esta factura', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(help_text='Enter a product name', max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.AddField(
            model_name='detalle_factura',
            name='factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facturacion.Factura'),
        ),
        migrations.AddField(
            model_name='detalle_factura',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facturacion.Producto'),
        ),
    ]