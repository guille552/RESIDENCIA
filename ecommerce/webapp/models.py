from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Modelo de Producto
class Producto(models.Model):
    producto_id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'

# Modelo de Pedido
class Pedido(models.Model):
    pedido_id = models.BigAutoField(primary_key=True)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ], default='pendiente')
    direccion_envio = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"Pedido {self.pedido_id} - Usuario {self.usuario_id}"

    class Meta:
        db_table = 'pedidos'

# Modelo de Artículo en el Pedido
class ArticuloPedido(models.Model):
    articulo_pedido_id = models.BigAutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='articulos')
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto_id.nombre}"

    class Meta:
        db_table = 'articulos_pedido'

# Modelo de Pago
class Pago(models.Model):
    pago_id = models.BigAutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('tarjeta', 'Tarjeta de crédito'),
        ('paypal', 'PayPal'),
        ('transferencia', 'Transferencia bancaria'),
    ])
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    transaccion_id = models.CharField(max_length=255, unique=True)
    fecha_pago = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pago {self.pago_id} - Pedido {self.pedido_id}"

    class Meta:
        db_table = 'pagos'

# Modelo de Reseña
class Reseña(models.Model):
    resena_id = models.BigAutoField(primary_key=True)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reseña {self.resena_id} - Producto {self.producto_id.nombre}"

    class Meta:
        db_table = 'reseñas'
