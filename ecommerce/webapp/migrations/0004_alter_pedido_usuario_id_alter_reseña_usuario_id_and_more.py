# Generated by Django 5.0.6 on 2024-09-21 20:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_delete_libro'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reseña',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedido',
            name='codigo_postal',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion_envio',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articulopedido',
            name='pedido_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='webapp.pedido'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='metodo_pago',
            field=models.CharField(choices=[('tarjeta', 'Tarjeta de crédito'), ('paypal', 'PayPal'), ('transferencia', 'Transferencia bancaria')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pago',
            name='transaccion_id',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('procesando', 'Procesando'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=50),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
