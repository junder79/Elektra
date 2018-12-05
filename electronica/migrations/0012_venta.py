# Generated by Django 2.1.3 on 2018-12-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronica', '0011_auto_20181202_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField()),
                ('cantidad_venta', models.CharField(max_length=2)),
                ('comentario_venta', models.CharField(max_length=200)),
                ('producto_vendido', models.ManyToManyField(to='electronica.Productos')),
                ('sucursal_venta', models.ManyToManyField(to='electronica.Tiendas')),
            ],
        ),
    ]
