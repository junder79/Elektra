# Generated by Django 2.1.3 on 2018-12-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_productos', models.CharField(choices=[('Electronica', 'Electronica'), ('Computacion', 'Computacion')], default='', max_length=30)),
                ('nombre_productos', models.CharField(max_length=200)),
                ('precio_productos', models.CharField(max_length=200)),
                ('descripcion_productos', models.TextField()),
            ],
        ),
    ]
