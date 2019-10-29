from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from core.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index.as_view(), name='index'),

    path('account/', include('django.contrib.auth.urls'), name='account'),

    path('enderecos/', enderecos.as_view(), name='enderecos'),
    path('add_endereco/', add_endereco.as_view(), name='add_endereco'),
    path('del_endereco/<int:id_endereco>/', del_endereco, name='del_endereco'),
    path('ajax/new_endereco/', new_endereco, name='new_endereco'),

    path('lojas/', lojas.as_view(), name='lojas'),
    path('add_loja/', add_loja.as_view(), name='add_loja'),
    path('del_loja/<int:id_loja>/', del_loja, name='del_loja'),
    path('ajax/new_loja/', new_loja, name='new_loja'),

    path('areas/', areas.as_view(), name='areas'),
    path('add_area/', add_area.as_view(), name='add_area'),
    path('del_area/<int:id_area>/', del_area, name='del_area'),
    path('ajax/new_area/', new_area, name='new_area'),
    
    path('gps/', gps.as_view(), name='gps'),
    path('ajax/valid_gps/', valid_gps, name='valid_gps'),
    
    ################################################################################
    # TURF  ########################################################################
    path('endereco_turf/', endereco_turf.as_view(), name='endereco_turf'),
    path('loja_turf/', loja_turf.as_view(), name='loja_turf'),
    path('area_turf/', area_turf.as_view(), name='area_turf'),
    path('gps_turf/', gps_turf.as_view(), name='gps_turf'),
    
    path('usuarios/', usuarios.as_view(), name='usuarios'),
    path('new_usuario/', new_usuario, name='new_usuario'),
]
