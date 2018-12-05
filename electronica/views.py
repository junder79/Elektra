from django.shortcuts import render, get_object_or_404
#Para redirigir las vistas 
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
#Importamos los Modelos de la base de datos a las vistas
from .models import Productos
from .models import Tiendas
from .models import Venta
from django.contrib.auth.models import User
from .forms import TiendasForm
from .forms import ProductosForm
from .forms import VentaForm
#MENSAJES
from django.contrib import messages
from django.db.models import Sum

def inicio(request):
    return render(request, 'aplicacion/inicio.html', {})


#Metodo que nos redirecciones a un sition para cada tipo de usuario


def redirigir(request):

    user = request.user
    tiendas=Tiendas.objects.filter()
    if user.has_perm('electronica.admin'):

    	return render(request, 'administrador/adm.tiendas.html', {'tiendas': tiendas})
    else:
        return render(request, 'vendedor/v.ventas.html',{'tiendas': tiendas})   


#Dos metodos ,el cual redirecciona a la pantalla de inicio depende el usuario

def administrador_tiendas(request):
    tiendas=Tiendas.objects.filter()
    return render(request, 'administrador/adm.tiendas.html', {'tiendas': tiendas})


def administrador_productos(request):
    productos = Productos.objects.filter()
    return render(request, 'administrador/adm.productos.html',  {'productos': productos})


def nueva_tienda(request):
    form = TiendasForm()
    return render(request, 'administrador/adm.agregar_tiendas.html', {'form': form})


#METODO PARA AGREGAR LA TIENDA 
def nueva_tienda(request): 
   if request.method == "POST":
       form = TiendasForm(request.POST or None)
       if form.is_valid():
           post = form.save(commit=True)
           post.save()
           messages.info(request, 'La Tienda fue agregada exitosamente')
           return redirect('adm.tiendas')
   else:
       form = TiendasForm()
   return render(request, 'administrador/adm.agregar_tiendas.html', {'form': form})


def nuevo_producto(request):
    form = ProductosForm()
    return render(request, 'administrador/adm.agregar_productos.html', {'form': form})

#METODO PARA AGREGAR PRODUCTOS
def nuevo_producto(request): 
   if request.method == "POST":
       form = ProductosForm(request.POST or None, request.FILES or None)
       if form.is_valid():
           post = form.save(commit=False)
           post.save()
           return redirect('adm.productos')
   else:
       form = ProductosForm()
   return render(request, 'administrador/adm.agregar_productos.html', {'form': form})
def vendedor_ventas(request):
    #OBJETO PRINCIPAL DE VENTAS 
    ventas = Venta.objects.filter()
    suma= Venta.objects.aggregate(Sum('cantidad_venta'))
    return render(request, 'vendedor/v.ventas.html', {'ventas':ventas , 'suma':suma})    


#METODO QUE NOS RETORNA LA PLANTILLA DE PRODUCTOS ASOCIADOS DE DICHA TIENDA
def vendedor_productos_asociados(request):
    #SE GUARDARA LA ID DEL USUARIO QUE ESTA ACTIVO , LUEGO DE ACUERO DE LA RELACION UNO A UNO , LA ID SE LA IGUAL AL ENCARGADO
    #COLOCANDO UN "WHERE"
    id_usuario_activo = request.user.id
     #OBJETO PRINCIPAL DE TIENDAS 
    tiendas=Tiendas.objects.filter(encargado=id_usuario_activo)
    return render(request, 'vendedor/v.ventas_productos.html', {'tiendas':tiendas})    



#METODO PARA REALIZAR UNA VENTA

def nueva_venta(request):
    form = VentaForm()
    return render(request, 'vendedor/v.ventas_agregar.html', {'form': form})      



def nueva_venta(request):
   if request.method == "POST":
       form = VentaForm(request.POST or None)
       if form.is_valid():
        
           post = form.save(commit=False)
           post.save()
           return redirect('v.ventas')
   else:
       form = VentaForm()
   return render(request, 'vendedor/v.ventas_agregar.html', {'form': form})


