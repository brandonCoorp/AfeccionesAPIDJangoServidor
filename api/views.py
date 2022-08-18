import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import PagosModelo
# Create your views here.

class PagoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            pago = list(PagosModelo.objects.filter(id=id).values())
            if len(pago)>0:
                pagoE = pago[0]   
                datos ={'message': "Success", 'pago': pagoE}
            else:
                datos ={'message': "Pago no enconctrado"}
            return JsonResponse(datos)
        else:
            pagos = list(PagosModelo.objects.values())
            if len(pagos)>0:
                   datos ={'message': "Success", 'pagos': pagos}
            else:
                   datos ={'message': "Pagos no enconctrados"}
            return JsonResponse(datos)

    def post(self, request):
        pago = json.loads(request.body)
        datos = {'message': "Success"}
        PagosModelo.objects.create(nombre=pago['nombre'], descripcion=pago['descripcion'], costo=pago['costo'])
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd= json.loads(request.body)
        Existepago = list(PagosModelo.objects.filter(id=id).values())
        if len(Existepago)>0:
                pago = PagosModelo.objects.get(id=id)
                pago.nombre= jd['nombre']
                pago.descripcion = jd['descripcion']
                pago.costo = jd['costo']
                pago.save() 
                datos ={'message': "Success"}
        else:
                datos ={'message': "Pago no enconctrado"}
        return JsonResponse(datos)
        
    def delete(self, request, id):
         Existepago = list(PagosModelo.objects.filter(id=id).values())
         if len(Existepago)>0:
                PagosModelo.objects.filter(id=id).delete()
                datos ={'message': "Success"}
         else:
                datos ={'message': "Pago no enconctrado"}
         return JsonResponse(datos)
    

class Diagnosticar(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            pago = list(PagosModelo.objects.filter(id=id).values())
            if len(pago)>0:
                pagoE = pago[0]   
                datos ={'message': "Success", 'pago': pagoE}
            else:
                datos ={'message': "Pago no enconctrado"}
            return JsonResponse(datos)
        else:
            pagos = list(PagosModelo.objects.values())
            if len(pagos)>0:
                   datos ={'message': "Success", 'pagos': pagos}
            else:
                   datos ={'message': "Pagos no enconctrados"}
            return JsonResponse(datos)

    def post(self, request):
        js = json.loads(request.body)
        c=js['a'] +js['b']
        datos = {'message': "Success", 'respuesta':c}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd= json.loads(request.body)
        Existepago = list(PagosModelo.objects.filter(id=id).values())
        if len(Existepago)>0:
                pago = PagosModelo.objects.get(id=id)
                pago.nombre= jd['nombre']
                pago.descripcion = jd['descripcion']
                pago.costo = jd['costo']
                pago.save() 
                datos ={'message': "Success"}
        else:
                datos ={'message': "Pago no enconctrado"}
        return JsonResponse(datos)
        
    def delete(self, request, id):
         Existepago = list(PagosModelo.objects.filter(id=id).values())
         if len(Existepago)>0:
                PagosModelo.objects.filter(id=id).delete()
                datos ={'message': "Success"}
         else:
                datos ={'message': "Pago no enconctrado"}
         return JsonResponse(datos)
        