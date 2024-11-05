from django.conf import settings
from django.db import models
from django.utils import timezone

# Modelo principal Calcetin
class Calcetin(models.Model):
    modelo = models.CharField(max_length=100)  # Define un tamaño máximo para CharField
    precio = models.FloatField(default=5.0)  # Precio del producto
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Fecha de creación

# Modelo de cliente que será el usuario o cliente que compra calcetines
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)  # Ampliado el límite de caracteres para el nombre
    contraseña = models.CharField(max_length=100)  # Contraseña del cliente
    saldo = models.FloatField(default=0.0)  # Dinero del cliente
    fecha_registro = models.DateTimeField(default=timezone.now)  # Fecha de registro
    valoracion = models.ManyToManyField(
        Calcetin, through='Votacion', related_name='voto_cliente'
    )  

# Votacion es una tabla intermedia entre Cliente y Calcetin donde se guarda la valoracion
class Votacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='votaciones')
    calcetin = models.ForeignKey(Calcetin, on_delete=models.CASCADE, related_name='votaciones')
    valoracion = models.IntegerField(default=0)  # Valor de la valoracion
    comentario = models.TextField(blank=True, null=True)  # Comentario del usuario
    fecha_votacion = models.DateTimeField(default=timezone.now)  # Fecha de votacion

# CuentaBanco para asociar una cuenta bancaria a un cliente
class CuentaBanco(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='banco_cliente')
    nombre = models.CharField(
        max_length=10,
        choices=[('C', 'Caixa'), ('B', 'BBVA'), ('U', 'UNICAJA'), ('I', 'ING')]
    )  # Opciones de banco
    numero_cuenta = models.CharField(max_length=24)  # Numero de cuenta del cliente
    creacion_cuenta = models.DateField(default=timezone.now)  # Fecha de creación de la cuenta
