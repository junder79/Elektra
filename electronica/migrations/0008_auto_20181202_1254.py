# Generated by Django 2.1.3 on 2018-12-02 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronica', '0007_tiendas_produc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiendas',
            name='produc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronica.Productos'),
        ),
    ]