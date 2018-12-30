from django.contrib import admin
from .models import Productos
from .models import Tiendas
from .models import Venta
from .models import Oferta
#Registrar el modelo en el Administrador de DJANGO

admin.site.register(Productos)
admin.site.register(Tiendas)
admin.site.register(Venta)
admin.site.register(Oferta)