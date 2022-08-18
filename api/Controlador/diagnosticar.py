import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class Diagnosticar(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        pass
       
    def post(self, request):
        js = json.loads(request.body)
        c=js['a'] +js['b']
        datos = {'message': "Success", 'respuesta':c}
        return JsonResponse(datos)
    
    def put(self, request, id):
       pass
        
    def delete(self, request, id):
         pass

    @csrf_exempt
    def Saludar(request):
          js = json.loads(request.body)
          c=js['a'] +js['b']
          datos = {'message': "Success", 'respuesta':c}
          return JsonResponse(datos)  