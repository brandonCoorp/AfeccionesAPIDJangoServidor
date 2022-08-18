import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..models import AdministradorModelo
# Create your views here.

class AdministradorControl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
     
    #ver y listar  Administrador(es)
    def get(self, request, id=0):
        if (id>0):
            administrador = list(AdministradorModelo.objects.filter(id=id).values())
            if len(administrador)>0:
                administradorE = administrador[0]   
                datos ={'message': "Success", 'administrador': administradorE}
            else:
                datos ={'message': "administrador no encontrado"}
            return JsonResponse(datos)
        else:
            administradors = list(AdministradorModelo.objects.values())
            if len(administradors)>0:
                   datos ={'message': "Success", 'administradores': administradors}
            else:
                   datos ={'message': "administradores no encontrados"}
            return JsonResponse(datos)

    #crear nuevo administrador
    def post(self, request):
        pass
    
    #actualizar  Administrador
    def put(self, request, id):
        jd= json.loads(request.body)
        existeadmin = list(AdministradorModelo.objects.filter(id=id).values())
        if len(existeadmin)>0:
                administrador = AdministradorModelo.objects.get(id=id)
                administrador.nombre= jd['nombre']
                administrador.apellido = jd['apellido']
                administrador.correo = jd['correo']
                administrador.contraseña = jd['contraseña']
                administrador.save() 
                datos ={'message': "Success"}
        else:
                datos ={'message': "Administrador no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
         pass
    
        