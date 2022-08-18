import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..models import FacturaModelo
# Create your views here.



class FacturaControl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #ver y listar factura(s)
    def get(self, request, id=0):
        if (id>0):
            factura = list(FacturaModelo.objects.filter(id=id).values())
            if len(factura)>0:
                facturaE = factura[0]   
                datos ={'message': "Success", 'factura': facturaE}
            else:
                datos ={'message': "factura no encontrado"}
            return JsonResponse(datos)
        else:
            facturas = list(FacturaModelo.objects.values())
            if len(facturas)>0:
                   datos ={'message': "Success", 'facturas': facturas}
            else:
                   datos ={'message': "facturas no encontrados"}
            return JsonResponse(datos)
    
    
    #Insertar factura
    def post(self, request):
       pass
    
    #Actualizar factura
    def put(self, request, id):
       pass

    #Eliminar factura   
    def delete(self, request, id):
         pass
