from django import forms
#Importamos el Modelo de Tiendas
from .models import Tiendas

#Importamos el modelo de Productos
from .models import Productos

#Modelo de ventas

from .models import Venta 

#Crear el formulario para agregar Tiendas

class TiendasForm(forms.ModelForm):
	class Meta:
		model=Tiendas
		fields=('nombre_tiendas','direccion_tiendas' , 'ciudad_tiendas' , 'comuna_tiendas','telefono_tiendas', 'correo_tiendas' ,'encargado' , 'productos',)	


#Formulario para agregar productos 

class ProductosForm(forms.ModelForm):
	class Meta:
		model=Productos
		fields=('imagen_productos','tipo_productos' , 'nombre_productos', 'precio_productos' , 'descripcion_productos',)


class VentaForm(forms.ModelForm):
	class Meta:
		model=Venta
		fields=('producto_vendido','fecha_venta','cantidad_venta','sucursal_venta','comentario_venta',)
		widgets = {
            'fecha_venta': forms.DateInput(attrs={'id': 'datetimepicker12'})
        }
