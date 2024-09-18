from django.db import models
from django.utils import timezone
# Create your models here.
class Usuario(models.Model):
    usuario_id = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255, unique=True)
    correo = models.EmailField(max_length=255, unique=True)
    contrasena_hash = models.CharField(max_length=255)
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'usuarios'

class Producto(models.Model):
    producto_id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'productos'

class Pedido(models.Model):
    pedido_id = models.BigAutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'pedidos'

class ArticuloPedido(models.Model):
    articulo_pedido_id = models.BigAutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'articulos_pedido'

class Pago(models.Model):
    pago_id = models.BigAutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    transaccion_id = models.CharField(max_length=255)
    fecha_pago = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'pagos'

class Reseña(models.Model):
    resena_id = models.BigAutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'reseñas'
