from django.shortcuts import render, get_object_or_404
#Para redirigir las vistas 
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
#Importamos los Modelos de la base de datos a las vistas
from .models import Productos
from .models import Tiendas
from .models import Venta
from .models import Oferta
from django.contrib.auth.models import User
from .forms import TiendasForm
from .forms import ProductosForm
from .forms import VentaForm
from .forms import OfertaForm
#MENSAJES
from django.contrib import messages
from django.db.models import Sum


# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('adm.tiendas')
    template_name = 'registration/signup.html'

def inicio(request):
    return render(request, 'aplicacion/inicio.html', {})


#Metodo que nos redirecciones a un sition para cada tipo de usuario


def redirigir(request):

    user = request.user
    tiendas=Tiendas.objects.filter()
    id_usuario_activo = request.user.id
    suma= list(Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo).aggregate(Sum('producto_vendido__precio_productos')).values())[0]    
    contar=Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo).count()
    ventas = Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo)
    form=VentaForm()
    if user.has_perm('electronica.admin'):

    	return render(request, 'administrador/adm.tiendas.html', {'tiendas': tiendas})
    else:
        return render(request, 'vendedor/v.ventas.html',{'ventas': ventas , 'suma':suma , 'contar':contar , 'form':form})   


#Dos metodos ,el cual redirecciona a la pantalla de inicio depende el usuario

def administrador_tiendas(request):
    tiendas=Tiendas.objects.filter()
    return render(request, 'administrador/adm.tiendas.html', {'tiendas': tiendas})


def administrador_productos(request):
    form =OfertaForm(request.POST or None  )
    productos = Productos.objects.filter()
    return render(request, 'administrador/adm.productos.html',  {'productos': productos , 'form':form})


def administrador_productos(request):
   if request.method == "POST":
       form =OfertaForm(request.POST or None  )
       productos =Productos.objects.filter()
       if form.is_valid():
        
           venta = form.save(commit=True)
           venta.save()
           return redirect('adm.productos')
   else:
       form = OfertaForm()
       productos =Productos.objects.filter()
   return render(request, 'administrador/adm.productos.html',  {'productos': productos , 'form':form})


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
           messages.info(request, 'El encargado elegido ya esta asociado a una Tienda')    
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
           messages.info(request, 'El producto fue agregado exitosamente')
           return redirect('adm.productos')
   else:
       form = ProductosForm()

   return render(request, 'administrador/adm.agregar_productos.html', {'form': form})


#Detalle del Post
def detalle_producto(request, pk):
    productos = get_object_or_404(Productos, pk=pk)
    return render(request, 'perris/adm.perro_post_detail.html', {'productos': productos})


#Modificar el POST de Perros y guardarlo
def editar_producto(request, pk):
    post = get_object_or_404(Productos, pk=pk)
    if request.method == "POST":
        form = ProductosForm(request.POST or None , request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # return redirect('detail_post_perro', pk=post.pk)
            messages.info(request, 'El Post se Actualizó')
            return redirect('adm.productos')
    else:
        form = ProductosForm(instance=post)
    return render(request, 'administrador/adm.oferta.html', {'form': form})


#------------------------CODIGO QUE NO SE UTILIZA BETA.----------------------
# #CREAR OFERTA
# def nueva_oferta(request):
#     form=OfertaForm()
#     return render(request, 'administrador/adm.oferta.html', {'form': form})


# #GUARDANDO LA OFERTA 

# def nueva_oferta(request):
#    if request.method == "POST":
#        form = OfertaForm(request.POST or None)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#            return redirect('adm.productos')
#    else:
#        form = OfertaForm()
#    return render(request, 'administrador/adm.oferta.html', {'form': form})        
def vendedor_ventas(request):
    #OBJETO PRINCIPAL DE VENTAS 
    id_usuario_activo = request.user.id
    suma= list(Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo).aggregate(Sum('producto_vendido__precio_productos')).values())[0]      
    ventas = Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo)
    contar=Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo).count()
    form=VentaForm()
    suma= Venta.objects.aggregate(Sum('producto_vendido__precio_productos'))
    return render(request, 'vendedor/v.ventas.html', {'ventas':ventas , 'suma':suma , 'form':form , 'contar':contar})    



def vendedor_ventas(request):
   if request.method == "POST":
       form = VentaForm(request.POST or None  )
       ventas = Venta.objects.filter()
       if form.is_valid():
        
           venta = form.save(commit=True)
           venta.save()
           return redirect('v.ventas')
   else:
       form = VentaForm()
   id_usuario_activo = request.user.id 
   suma= list(Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo).aggregate(Sum('producto_vendido__precio_productos')).values())[0]    
   ventas = Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo)
   contar=Venta.objects.filter(sucursal_venta__encargado=id_usuario_activo).count()
   return render(request, 'vendedor/v.ventas.html', {'ventas':ventas , 'suma':suma , 'form':form , 'contar':contar})  

#METODO QUE NOS RETORNA LA PLANTILLA DE PRODUCTOS ASOCIADOS DE DICHA TIENDA
def vendedor_productos_asociados(request):
    #SE GUARDARA LA ID DEL USUARIO QUE ESTA ACTIVO , LUEGO DE ACUERO DE LA RELACION UNO A UNO , LA ID SE LA IGUAL AL ENCARGADO
    #COLOCANDO UN "WHERE"
    id_usuario_activo = request.user.id
     #OBJETO PRINCIPAL DE TIENDAS 
    tiendas=Tiendas.objects.filter(encargado=id_usuario_activo)
    return render(request, 'vendedor/v.ventas_productos.html', {'tiendas':tiendas})    


def ventas_ofertas(request):
    id_usuario_activo=request.user.id
    ofertas = Oferta.objects.filter(tienda_oferta__encargado=id_usuario_activo)
    return render (request, 'vendedor/v.ofertas.html',  {'ofertas': ofertas})



