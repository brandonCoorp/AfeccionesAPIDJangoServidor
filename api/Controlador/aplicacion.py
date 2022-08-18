import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..models import AplicaciónModelo
# Create your views here.

class AplicacionControl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
     
    #ver y listar  Aplicacion(es)
    def get(self, request, id=0):
        if (id>0):
            aplicacion = list(AplicaciónModelo.objects.filter(id=id).values())
            if len(aplicacion)>0:
                aplicacionE = aplicacion[0]   
                datos ={'message': "Success", 'aplicacion': aplicacionE}
            else:
                datos ={'message': "aplicacion no encontrado"}
            return JsonResponse(datos)
        else:
            aplicacions = list(AplicaciónModelo.objects.values())
            if len(aplicacions)>0:
                   datos ={'message': "Success", 'aplicaciones': aplicacions}
            else:
                   datos ={'message': "aplicaciones no encontrados"}
            return JsonResponse(datos)

    #crear nuevo aplicacion
    def post(self, request):
        pass
    
    #actualizar  Aplicacion
    def put(self, request, id):
        jd= json.loads(request.body)
        existeapp = list(AplicaciónModelo.objects.filter(id=id).values())
        if len(existeapp)>0:
                aplicacion = AplicaciónModelo.objects.get(id=id)
                aplicacion.nombre= jd['nombre']
                aplicacion.logo = jd['logo']
                aplicacion.descripcion = jd['descripcion']
                aplicacion.correo = jd['correo']
                aplicacion.save() 
                datos ={'message': "Success"}
        else:
                datos ={'message': "aplicacion no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
         pass
    
        