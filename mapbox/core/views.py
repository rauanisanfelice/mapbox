from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.db.models import Max

from core.models import *

import pyproj
import json

from shapely.geometry import Point, Polygon
from functools import partial
from shapely.ops import transform
from shapely.geometry import Point

proj_wgs84 = pyproj.Proj(init='epsg:4326')

class index(View):
    retorno = 'index.html'
    def get(self, request):
        return render(request, self.retorno)


################################################
#  ENDEREÇOS 
class enderecos(View):
    retorno = 'enderecos.html'
    def get(self, request):
        return render(request, self.retorno, {'enderecos': ENDERECOS.objects.all()})


class add_endereco(View):
    retorno = 'add_endereco.html'
    def get(self, request):
        return render(request, self.retorno)


def new_endereco(request):
    retorno = 'enderecos'
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)
    raio = request.GET.get('raio', None)
    try:
        modelo = ENDERECOS(LATITUDE=latitude, LONGITUDE=longitude, RAIO=raio, ATIVO='True')
        modelo.save()
    except:
        pass
    return redirect(retorno)


def del_endereco(request, id_endereco):
    retorno = 'enderecos'
    try:
        modelo = ENDERECOS.objects.get(id=id_endereco)
        modelo.delete()
    except:
        pass
    return redirect(retorno)  


################################################
#  LOJAS

class lojas(View):
    retorno = 'lojas.html'
    def get(self, request):
        return render(request, self.retorno, {'lojas': LOJAS.objects.all()})


class add_loja(View):
    retorno = 'add_loja.html'
    def get(self, request):
        return render(request, self.retorno)


def new_loja(request):
    retorno = 'lojas'
    descricao = request.GET.get('descricao', None)
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)
    raio = request.GET.get('raio', None)
    try:
        modelo = LOJAS(DESCRICAO=descricao, LATITUDE=latitude, LONGITUDE=longitude, RAIO=raio)
        modelo.save()
    except:
        pass
    return redirect(retorno)      


def del_loja(request, id_loja):
    retorno = 'lojas'
    try:
        modelo = LOJAS.objects.get(id=id_loja)
        modelo.delete()
    except:
        pass
    return redirect(retorno)  

################################################
#  AREAS

class areas(View):
    retorno = 'areas.html'
    def get(self, request):
        return render(request, self.retorno, {
            'areas': AREAS.objects.all().order_by('ID_AREA', 'ORDEM'),
            'areas_dist': AREAS.objects.distinct('ID_AREA', 'DESCRICAO').all(),
        })


class add_area(View):
    retorno = 'add_area.html'
    def get(self, request):
        id_area = AREAS.objects.aggregate(Max('ID_AREA'))
        if id_area['ID_AREA__max'] == None:
            id_area = 1
        else:
            id_area = int(id_area['ID_AREA__max']) + 1
        return render(request, self.retorno, {'id_max': id_area})


def new_area(request):
    retorno = 'areas.html'
    id_area = request.GET.get('id_area', None)
    descricao = request.GET.get('descricao', None)
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)
    ordem = request.GET.get('ordem', None)
    try:
        modelo = AREAS(ID_AREA=id_area, DESCRICAO=descricao, LATITUDE=latitude, LONGITUDE=longitude, ORDEM= ordem, ATIVO='True')
        modelo.save()
    except:
        pass
    return render(request, retorno)


def del_area(request, id_area):
    retorno = 'areas'
    try:
        modelo = AREAS.objects.filter(ID_AREA=id_area)
        modelo.delete()
    except:
        pass
    return redirect(retorno)

################################################
#  AREAS

class gps(View):
    retorno = 'gps.html'
    def get(self, request):
        return render(request, self.retorno, {
            'areas': AREAS.objects.all().order_by('ID_AREA', 'ORDEM'),
            'areas_dist': AREAS.objects.distinct('ID_AREA', 'DESCRICAO').all(),
            'lojas': LOJAS.objects.all(),
            'enderecos': ENDERECOS.objects.all(),
        })


def geodesic_point_buffer(lat, lon, km):
    # Azimuthal equidistant projection
    aeqd_proj = '+proj=aeqd +lat_0={lat} +lon_0={lon} +x_0=0 +y_0=0'
    project = partial(
        pyproj.transform,
        pyproj.Proj(aeqd_proj.format(lat=lat, lon=lon)),
        proj_wgs84)
    buf = Point(0, 0).buffer(km * 1000)  # distance in metres
    return transform(project, buf).exterior.coords[:]


def valid_gps(request):

    # Create Point 
    longitude = request.POST.get('long_point', None)
    latitude = request.POST.get('lat_point', None)
    p1 = Point(float(longitude), float(latitude))

    ########################################################
    # CREATE POLYGNO DE AREAS ##############################
    areas = AREAS.objects.all().order_by('ID_AREA', 'ORDEM')
    polygno = []
    list_polygno = []
    for i in range(len(areas)):
        if(areas[i].ATIVO == True):
            if(i == 0):
                last_id = areas[i].ID_AREA
            
            if(last_id == areas[i].ID_AREA):
                temp = []
                temp.append(float(areas[i].LATITUDE))
                temp.append(float(areas[i].LONGITUDE))
                polygno.append(temp)
            else:
                list_polygno.append(polygno)
                temp = []
                temp.append(float(areas[i].LATITUDE))
                temp.append(float(areas[i].LONGITUDE))
                polygno = []
                polygno.append(temp)
                last_id = areas[i].ID_AREA
    
    
    ########################################################
    # CREATE POLYGNO DE ENDERECOS ##########################
    enderecos = ENDERECOS.objects.all()
    for z in range(len(enderecos)):
        if(enderecos[z].ATIVO == True):
            A = geodesic_point_buffer(float(enderecos[z].LATITUDE), float(enderecos[z].LONGITUDE), int(enderecos[z].RAIO))
            list_polygno.append(A)
    
    ########################################################
    # CREATE POLYGNO DE LOJAS ##############################
    lojas = LOJAS.objects.all()
    for y in range(len(lojas)):
        B = geodesic_point_buffer(float(lojas[y].LATITUDE), float(lojas[y].LONGITUDE), int(lojas[y].RAIO))
        list_polygno.append(B)

    ########################################################
    # VALIDA POLYGNOS ######################################
    data = {}
    list_polygno.append(polygno)
    for pol in list_polygno:
        poly = Polygon(pol)

        if (p1.within(poly)):
            data['result'] = 1
            break
        else:
            data['result'] = 0

    return HttpResponse(json.dumps(data), content_type="application/json")

################################################
#  TURF  #######################################

class endereco_turf(View):
    retorno = 'enderecos_turf.html'
    def get(self, request):
        return render(request, self.retorno, {'enderecos': ENDERECOS.objects.all()})


class loja_turf(View):
    retorno = 'lojas_turf.html'
    def get(self, request):
        return render(request, self.retorno, {'lojas': LOJAS.objects.all()})


class area_turf(View):
    retorno = 'areas_turf.html'
    def get(self, request):
        return render(request, self.retorno, {
            'areas': AREAS.objects.all().order_by('ID_AREA', 'ORDEM'),
            'areas_dist': AREAS.objects.distinct('ID_AREA', 'DESCRICAO').all(),
        })


class gps_turf(View):
    retorno = 'gps_turf.html'
    def get(self, request):
        return render(request, self.retorno, {
            'areas': AREAS.objects.all().order_by('ID_AREA', 'ORDEM'),
            'areas_dist': AREAS.objects.distinct('ID_AREA', 'DESCRICAO').all(),
            'lojas': LOJAS.objects.all(),
            'enderecos': ENDERECOS.objects.all(),
        })

################################################

class usuarios(View):
    retorno = 'usuarios.html'
    def get(self, request):
        users = User.objects.all()
        return render(request, self.retorno, {
            'usuarios': users,
        })

def new_usuario(request):
    retorno = 'new_usuario.html'

    if request.method == 'GET':
        return render(request, retorno)

    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario', None)
        usuario = User.objects.get(id=id_usuario)
    
        return render(request, retorno, {
            'usuario': usuario,
        })