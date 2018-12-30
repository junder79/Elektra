from django.db import models
from django.contrib.auth.models import User




tipo_productos= (
    ('Electronica', 'Electronica'),
    ('Computacion', 'Computacion'),
)


#REVISAR TABLA
class Productos(models.Model):

    tipo_productos= models.CharField(max_length=30, choices=tipo_productos, default='')
    imagen_productos=models.FileField(blank=True, null=True)
    nombre_productos = models.CharField(max_length=200)
    precio_productos = models.CharField(max_length=200)
    descripcion_productos=models.TextField()


    def __str__(self):
        return self.nombre_productos


#TABLA TEINDAS

class Tiendas(models.Model):

	nombre_tiendas=models.CharField(max_length=200)
	direccion_tiendas=models.CharField(max_length=200)
	ciudad_tiendas=models.CharField(max_length=200)
	comuna_tiendas=models.CharField(max_length=200)
	telefono_tiendas=models.CharField(max_length=200)
	correo_tiendas=models.CharField(max_length=200)
	#Uno a Uno , ya que la tienda tiene que estar unida a un vendedor
	encargado=models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)

	#Mucho a Muchos ,ya que las tiendas pueden tener el mismo prtoducto y el producto puede estar en muchas tiendas
	productos=models.ManyToManyField(Productos)
	def __str__(self):
		return self.comuna_tiendas
    
class Venta(models.Model):
	
	producto_vendido=models.ForeignKey(Productos,null=False,blank=False,on_delete=models.CASCADE)
	fecha_venta=models.DateTimeField(auto_now_add=True)
	cantidad_venta=models.CharField(max_length=2)
	sucursal_venta=models.ForeignKey(Tiendas,null=False,blank=False,on_delete=models.CASCADE)
	comentario_venta=models.CharField(max_length=200)


class Oferta(models.Model):
	precio_producto=models.CharField(max_length=200)
	tienda_oferta=models.ForeignKey(Tiendas,null=False,blank=False,on_delete=models.CASCADE)
	producto_oferta=models.OneToOneField(Productos,null=False,blank=False,on_delete=models.CASCADE)