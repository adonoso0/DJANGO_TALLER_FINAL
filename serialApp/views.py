from django.shortcuts import render, redirect
from .serializers import InscritosSerializer, InstitucionesSerializers
from .models import Inscritos, Instituciones
from .forms import FormInscritos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404, JsonResponse


def index(request):
    return render(request, 'serialApp/index.html')

def listaAPI(request):
    return render(request, 'serialApp/listaAPI.html')    


def listadoInscripciones(request):
    ins = Inscritos.objects.all()
    data = {'ins': ins}
    return render(request, 'serialApp/listaInscripciones.html', data)


def agregarReserva(request):
    form = FormInscritos()
    if request.method == "POST":
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return listadoInscripciones(request)
    data = {'form': form}
    return render(request, 'serialApp/agregarReserva.html', data)


def eliminarReserva(request, id):
    ins = Inscritos.objects.get(id=id)
    ins.delete()
    return redirect('/inscripciones')


def actualizarReserva(request, id):
    ins = Inscritos.objects.get(id=id)
    form = FormInscritos(instance=ins)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return listadoInscripciones(request)
    data = {'form': form}
    return render(request, 'serialApp/actualizarReserva.html', data)


def jsonInscritos(request):
    ins = Inscritos.objects.all()
    data = {'DJANGO_SEMINARIO': list(ins.values(
        'id', 'nombre', 'institucion', 'telefono', 'fechareserva', 'horareserva', 'estado', 'observacion'))}

    return JsonResponse(data)


@api_view(['GET', 'POST'])
def InstitucionLista(request):
    if request.method == 'GET':
        inst = Instituciones.objects.all()
        serial = InstitucionesSerializers(inst, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionesSerializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def InstitucionDetalle(request, id):
    try:
        inst = Instituciones.objects.get(pk=id)
    except inst.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionesSerializers(inst)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InscritosSerializer(inst, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        inst.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InscritosLista(APIView):
    def get(self, request):
        ins = Inscritos.objects.all()
        serial = InscritosSerializer(ins, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class InscritosDetalle(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(id=pk)
        except Inscritos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins)
        return Response(serial.data)

    def put(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ins = self.get_object(pk)
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
