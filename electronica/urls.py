from django.conf.urls import include, url
from electronica import views
from django.views.generic import TemplateView
from django.urls import path, include 
urlpatterns = [
	url(r'^$', views.inicio),
	url('redirigir', views.redirigir, name="redirigir"),
	#URLS DE ADMINISTRADOR
    url('tiendas',views.administrador_tiendas, name="adm.tiendas" ),
    url('productos',views.administrador_productos, name="adm.productos" ),	
	url('shop', views.nueva_tienda, name='nueva_tienda'),
	url('products', views.nuevo_producto, name='nuevo_producto'),
    #URLS DEL VENDEDOR    	
    url('ventas',views.vendedor_ventas, name="v.ventas" ),	
    url('productitos',views.vendedor_productos_asociados, name="v.ventas_productos" ),	
    # url('addventa', views.nueva_venta, name='nueva_venta'),
          url(r'^sw.js', (TemplateView.as_view(
        template_name="sw.js",
        content_type='application/javascript',
    )), name='sw.js'),
    

]