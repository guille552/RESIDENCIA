from django.contrib import admin
from .models import Usuario, Producto, Pedido, ArticuloPedido, Pago, Reseña
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ArticuloPedido)
admin.site.register(Pago)
admin.site.register(Reseña)
