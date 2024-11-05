from django.urls import path,re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ultimo_voto',views.ultimo_voto,name='ultimo_voto'),
    path('mayor_tres/<int:valoracion>/',views.mayor_tres,name='mayor_tres'),
    path('votacion_nula',views.votacion_nula,name='votacion_nula'),
    path('cuentas_bancarias/', views.cuentas_bancarias, name='cuentas_bancarias'),
    path('media_votos/', views.media_votos, name='media_votos'),
]
