import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..models import EnfermedadModelo
# Create your views here.



class EnfermedadControl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #ver y listar Enfermedad(es)
    def get(self, request, id=0):
        if (id>0):
            enfermedad = list(EnfermedadModelo.objects.filter(id=id).values())
            if len(enfermedad)>0:
                enfermedadE = enfermedad[0]   
                datos ={'message': "Success", 'enfermedad': enfermedadE}
            else:
                datos ={'message': "enfermedad no encontrado"}
            return JsonResponse(datos)
        else:
            enfermedades = list(EnfermedadModelo.objects.values())
            if len(enfermedades)>0:
                   datos ={'message': "Success", 'enfermedades': enfermedades}
            else:
                   datos ={'message': "enfermedades no encontrados"}
            return JsonResponse(datos)
    
    #buscar enfermedad por nombre
    def getbyNombre(self, nombre ="na"):
        datos = ""
        if(nombre != "na"):
            enfermedad = list(EnfermedadModelo.objects.filter(nombre=nombre).values())
            if len(enfermedad)>0:
                datos ={'message': "Success", 'enfermedad': enfermedad}
            else:
                datos = {'message': "no encontrado"}  
        else:
            datos = {'message': "no encontrado"}
        return JsonResponse(datos)


    #Insertar Enfermedad
    def post(self, request):
        enfermedad = json.loads(request.body)
        datos = {'message': "Success"}
        EnfermedadModelo.objects.create(nombre=enfermedad['nombre'], descripcion=enfermedad['descripcion'], imagen=enfermedad['imagen'], cant_imagen=enfermedad['cant_imagen'], aplicacion_id=enfermedad['aplicacion_id'])
        return JsonResponse(datos)
    
    #Actualizar Enfermedad
    def put(self, request, id):
        jd= json.loads(request.body)
        Existeenfermedad = list(EnfermedadModelo.objects.filter(id=id).values())
        if len(Existeenfermedad)>0:
                enfermedad = EnfermedadModelo.objects.get(id=id)
                enfermedad.nombre= jd['nombre']
                enfermedad.descripcion = jd['descripcion']
                enfermedad.imagen = jd['imagen']
                enfermedad.cant_imagen = jd['cant_imagen']
                enfermedad.aplicacion_id = jd['aplicacion_id']
                enfermedad.save() 
                datos ={'message': "Success"}
        else:
                datos ={'message': "enfermedad no encontrado"}
        return JsonResponse(datos)

    #Eliminar Enfermedad   
    def delete(self, request, id):
         Existeenfermedad = list(EnfermedadModelo.objects.filter(id=id).values())
         if len(Existeenfermedad)>0:
                EnfermedadModelo.objects.filter(id=id).delete()
                datos ={'message': "Success"}
         else:
                datos ={'message': "enfermedad no encontrado"}
         return JsonResponse(datos)
    
