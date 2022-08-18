import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..models import DiagnosticoModelo
# Create your views here.



class DiagnosticoControl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #ver y listar diagnostico(es)
    def get(self, request, id=0):
        if (id>0):
            diagnostico = list(DiagnosticoModelo.objects.filter(id=id).values())
            if len(diagnostico)>0:
                diagnosticoE = diagnostico[0]   
                datos ={'message': "Success", 'diagnostico': diagnosticoE}
            else:
                datos ={'message': "diagnostico no encontrado"}
            return JsonResponse(datos)
        else:
            diagnosticos = list(DiagnosticoModelo.objects.values())
            if len(diagnosticos)>0:
                   datos ={'message': "Success", 'diagnosticos': diagnosticos}
            else:
                   datos ={'message': "diagnosticos no encontrados"}
            return JsonResponse(datos)
    
    
    #Insertar diagnostico  no es por request ver por variable pasada por otra funcion y insertar una factura
    def post(self, request):
        diagnostico = json.loads(request.body)
        datos = {'message': "Success"}
        DiagnosticoModelo.objects.create(resultado=diagnostico['resultado'], imagen=diagnostico['imagen'], fecha=diagnostico['fecha'], enfermedad_id=diagnostico['enfermedad_id'], paciente_id=diagnostico['paciente_id'], consulta_id=diagnostico['consulta_id'])
        
        return JsonResponse(datos)
    
    #Actualizar diagnostico
    def put(self, request, id):
       pass

    #Eliminar diagnostico   
    def delete(self, request, id):
         pass
    def obtenerDiagnosticoUser(self,id=0):
        datos = {'message': "Id de paciente no encontrado"}
        if(id>0):
            diagnostico = list(DiagnosticoModelo.objects.filter(paciente_id=id).values())
            print(diagnostico)
            if len(diagnostico)>0:
                   datos ={'message': "Success", 'diagnosticos': diagnostico}
            else:
                   datos ={'message': "diagnosticos no encontrados"}
        return JsonResponse(datos)

