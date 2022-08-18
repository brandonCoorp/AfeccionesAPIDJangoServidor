import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
import jwt, datetime

from ..serializers import PacienteSerializer

#import de Modelos
from ..models import PacienteModelo
# Create your views here.

class PacienteControl(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
     
    #ver y listar  Paciente(s)
    def get(self, request, id=0):
        if (id>0):
            paciente = list(PacienteModelo.objects.filter(id=id).values())
            if len(paciente)>0:
                pacienteE = paciente[0]   
                datos ={'message': "Success", 'paciente': pacienteE}
            else:
                datos ={'message': "paciente no encontrado"}
            return JsonResponse(datos)
        else:
            pacientes = list(PacienteModelo.objects.values())
            if len(pacientes)>0:
                   datos ={'message': "Success", 'pacientes': pacientes}
            else:
                   datos ={'message': "pacientes no encontrados"}
            return JsonResponse(datos)

    #crear nuevo Paciente
    def post(self, request):
        paciente = json.loads(request.body)
        datos = {'message': "Success"}
        PacienteModelo.objects.create_user(email=paciente['email'], user_name=paciente['user_name'],
        password=paciente['password'],
        nombre=paciente['nombre'], apellido=paciente['apellido'], edad=paciente['edad'], sexo=paciente['sexo'])
        return JsonResponse(datos)


    @csrf_exempt
    def LoginPaciente(request):
         #print(request)
         user = json.loads(request.body)
         email = user['email']
         password = user['password']
         datos = {'message': "Success"}
         paciente = PacienteModelo.objects.filter(email = email).first()

         if paciente is None:
            datos ={'message': "paciente no encontrado"}
            return JsonResponse(datos)

         if not paciente.check_password(password):
            datos ={'message': "Contraseña Incorrecta"} 
            return JsonResponse(datos)

         payload = {
            'id' : paciente.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
         }   
         token = jwt.encode(payload, 'secret', algorithm='HS256')
         datos ={'jwt': token}
         return JsonResponse(datos)




    #actualizar  Paciente
    def put(self, request, id):
        jd= json.loads(request.body)
        existepaciente = list(PacienteModelo.objects.filter(id=id).values())
        if len(existepaciente)>0:
                paciente = PacienteModelo.objects.get(id=id)
                paciente.nombre= jd['nombre']
                paciente.apellido = jd['apellido']
                paciente.edad = jd['edad']
                paciente.sexo = jd['sexo']
                paciente.correo = jd['correo']
                paciente.contraseña = jd['contraseña']
                paciente.estado = jd['estado']   
                paciente.save() 
                datos ={'message': "Success"}
        else:
                datos ={'message': "Paciente no encontrado"}
        return JsonResponse(datos)

    #Eliminar  Paciente    
    def delete(self, request, id):
         Existepaciente = list(PacienteModelo.objects.filter(id=id).values())
         if len(Existepaciente)>0:
                PacienteModelo.objects.filter(id=id).delete()
                datos ={'message': "Success"}
         else:
                datos ={'message': "paciente no encontrado"}
         return JsonResponse(datos)
    
class LoginControl(APIView):
        def post(self, request):
         #print(request)
         user = json.loads(request.body)
         email = user['email']
         password = user['password']
         datos = {'message': "Success"}
         paciente = PacienteModelo.objects.filter(email = email).first()

         if paciente is None:
            raise AuthenticationFailed('Paciente no encontrado')

         if not paciente.check_password(password):
            raise AuthenticationFailed('Contraseña Incorrecta')


         payload = {
            'id' : paciente.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
         }   
         token = jwt.encode(payload, 'secret', algorithm='HS256')
         respuesta = Response()
         respuesta.set_cookie(key='jwt', value=token, httponly=True)
         respuesta.data ={'jwt': token,'id':paciente.id, 'nombre':paciente.nombre, 'detail': "logeado"}
         return respuesta

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('No Autenticado')
            
        try:
            payload= jwt.decode(token,'secret', algorithms=['HS256'])
        
        except jwt.jwt.ExpiredSignatureError:
            raise AuthenticationFailed('No Autenticado')
        
        paciente = PacienteModelo.objects.filter(id = payload['id']).first()
        serializado = PacienteSerializer(paciente)
        return Response(serializado.data)



class LogoutControl(APIView):
    def post(self,request):
        respuesta = Response()
        respuesta.delete_cookie('jwt')
        respuesta.data = {'message': 'Success' }
        return respuesta

