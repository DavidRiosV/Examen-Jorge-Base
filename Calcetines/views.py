from django.shortcuts import render
from django.db.models import Q,Prefetch
from django.db.models import Avg
from .models import Calcetin,Cliente,Votacion,CuentaBanco
from django.shortcuts import render

# Create your views here.

# Menu principal para acceder a los enlaces
def index(request):
    return render(request, 'index.html') 

# 1 El último voto que se realizó en un modelo principal en concreto, y mostrar el comentario, la votación e información del usuario o cliente que lo realizó: 1.5 puntos
# Solo muestra el ultimo en general pero no del modelo que quieres
def ultimo_voto(request):
    voto = Votacion.objects.order_by('-fecha_votacion')[:1]
    return render(request, 'ultimo_voto.html',{"voto":voto})

# 2 Todos los modelos principales que tengan votos con una puntuación numérica menor a 3 y que realizó un usuario o cliente en concreto: 1.5 puntos
# modelos principales que tengan votos con una puntuación numérica menor a 3 
def mayor_tres(request,valoracion):
    mayor =  Votacion.objects.filter(valoracion__lt=valoracion) #__lt menor que el que le paso como parametro, en este caso 3
    return render(request, 'mayor_tres.html',{"mayor":mayor})

# 3 Todos los usuarios o clientes que no han votado nunca y mostrar información sobre estos usuarios y clientes al completo: 1.5 puntos
# No funciona (Dara error)
def votacion_nula(request):
    comentario = Votacion.objects.all()
    comentario = comentario.filter(comentario=None)
    return render(request, ' votacion_nula.html',{"comentario":comentario})

# 4 Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el propietario tenga un nombre que contenga un texto en concreto, por ejemplo “Juan”: 1.5 puntos
# Funciona y muestra solo los clientes de caixa y  unicaja (C y U)
def cuentas_bancarias(request):
    cuenta = CuentaBanco.objects.filter(Q(nombre = 'C') | Q(nombre = 'U')).all()
    return render(request, 'cuentas_bancarias.html', {'cuenta': cuenta})

# 5 Obtener los votos de los usuarios que hayan votado a partir del 2023 con una puntuación numérica igual a 5  y que tengan asociada una cuenta bancaria. 1.5 puntos
# crear un filtro de year 2023 y otro que diga que voto debe ser = 5

# 6 Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5: 1.5 punto
def media_votos(request):   
    votos = Votacion.objects.aggregate(Avg('valoracion'))
    media = votos['votos media']
    votos_filtrados = Calcetin.objects.filter(valoracion=media)
    return render(request, 'media_votos.html', {'votos': votos, 'media': media, 'votos_filtrados': votos_filtrados})

# Páginas de Error
def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)


#Consultas:
# 6 Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5: 1.5 punto
# mostra los modeos que sumando su valoracion de mas de 2.5
