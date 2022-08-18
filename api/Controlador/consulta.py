from cgitb import reset
import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import jsonschema

from ..serializers import ConsultaSerializer, DiagnosticoSerializer
from ..models import ConsultaModelo, DiagnosticoModelo, PacienteModelo
from ..models import RespondeModelo
from ..models import EnfermedadModelo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
#import numpy as np
#from keras.utils import load_img, img_to_array
#from keras.models import load_model

#import cv2
import os


class UploadImagen(APIView):
    parser_classes = [MultiPartParser, FormParser]
    #@csrf_exempt
    def post(self, request, format=None):
        serializar = ConsultaSerializer(data= request.data)
        datos ={'message': "Success"}
        enfermedad=request.data['enfermedad']
        paciente_id =request.data['paciente_id']

        if serializar.is_valid(): 
            serializar.save()
            consulta = ConsultaModelo.objects.latest('id')
            Diagnosticar.guardar(enfermedad,paciente_id, consulta)
        else:
            datos ={'message': "No se pudo registrar su consulta"}
       
        return JsonResponse(datos)



class Diagnosticar(APIView):
    def guardar(enfermedad, paciente, consulta):
        enfermedad = EnfermedadModelo.objects.get(nombre=enfermedad)
        paciente = PacienteModelo.objects.filter(id=paciente).first()
        DiagnosticoModelo.objects.create(
           resultado =enfermedad.nombre, imagen=consulta.imagen, 
           consulta_id=consulta, enfermedad_id=enfermedad, paciente_id= paciente )

    def predecir(file):
      pass




class ConsultaControl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #ver y listar consulta(s)
    def get(self, request, id=0):
        if (id>0):
            consulta = list(ConsultaModelo.objects.filter(id=id).values())
            if len(consulta)>0:
                consultaE = consulta[0]   
                datos ={'message': "Success", 'consulta': consultaE}
            else:
                datos ={'message': "consulta no encontrado"}
            return JsonResponse(datos)
        else:
            consultas = list(ConsultaModelo.objects.values())
            if len(consultas)>0:
                   datos ={'message': "Success", 'consultas': consultas}
            else:
                   datos ={'message': "consultas no encontrados"}
            return JsonResponse(datos)
    
    
    #Insertar consulta    Averiguar obtener varias respuestaa y obtner id ultima consulta
    def post(self, request):
        consulta = json.loads(request.body)
        datos = {'message': "Success"}
        ConsultaModelo.objects.create(imagen=consulta['imagen'], fecha=consulta['fecha'], estado=consulta['estado'], paciente_id=consulta['paciente_id'])
        consulta =ConsultaModelo.objects.last()
        #print(consulta)
        RespondeModelo.objects.create(respuestas=consulta['respuestas'], consulta_id=consulta.id, paciente_id=consulta['paciente_id'])
        return JsonResponse(datos)


    #Actualizar consulta
    def put(self, request, id):
         pass

    #Eliminar consulta   
    def delete(self, request, id):
         pass
    
