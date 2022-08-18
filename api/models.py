from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

def upload_to(instance, filename):
    id = instance.paciente_id
    filename = id.nombre + '.jpg'
    return 'enfermedad/{filename}'.format(filename=filename)

def upload_toEnfermedad(instance, filename):
    #id = instance.paciente_id
    nombre = instance.nombre
    filename = nombre + '.jpg'
    return 'enfermedad/{filename}'.format(filename=filename)


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, user_name, nombre, password, **other_fields):
        if not email:
            raise ValueError(_('Correo invalido'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, nombre=nombre, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, user_name, nombre, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('edad',18)

        if other_fields.get('is_staff') is not True:
            raise ValueError('No es un Administrador')
        return self.create_user(email, user_name, nombre, password, **other_fields)



class PacienteModelo(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50, blank=True)
    apellido = models.CharField(max_length=100, blank=True)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=2, blank=True)
    email = models.EmailField(_('correo electronico'),max_length=50, blank=True, unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','nombre']

    def __str__(self): 
        return self.user_name

    class Meta:
        db_table = 'paciente'


class AdministradorModelo(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=100, null=False)
    contraseña = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=50, null=False, unique=True)
     
    class Meta:
        db_table = 'administrador'

class AplicaciónModelo(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    logo = models.CharField(max_length=250, null=False)
    descripcion = models.TextField(null=False)
    correo = models.CharField(max_length=50, null=False, unique=True)   
 
    class Meta:
        db_table = 'aplicación'


class PagosModelo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=False)
    costo = models.FloatField()
    aplicacion_id = models.ForeignKey(AplicaciónModelo, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'pagos'


class EnfermedadModelo(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True)
    descripcion = models.TextField(null=False)
    imagen = models.ImageField(
        _("Imagen"), upload_to=upload_toEnfermedad, default = 'media/default.jpg'
     )
    cant_imagen = models.PositiveIntegerField()
    tratamiento = models.TextField(max_length=250, null=False)
    aplicacion_id = models.ForeignKey(AplicaciónModelo, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'enfermedad'


class ConsultaModelo(models.Model):
    imagen = models.ImageField(
        _("Imagen"), upload_to=upload_to, default = 'media/default.jpg'
    )
    estado = models.PositiveIntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    paciente_id = models.ForeignKey(PacienteModelo, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'consulta'


class RespondeModelo(models.Model):
    respuesta = models.CharField(max_length=250, null=False, unique=True)
    paciente_id = models.ForeignKey(PacienteModelo, on_delete=models.CASCADE, null=False)
    consulta_id = models.ForeignKey(ConsultaModelo, on_delete=models.CASCADE, null=False)

    
    class Meta:
        db_table = 'responde'


class DiagnosticoModelo(models.Model):
    resultado = models.TextField(null=False)
    imagen = models.CharField(max_length=250, null=False)   
    fecha = models.DateTimeField(default=timezone.now)
    paciente_id = models.ForeignKey(PacienteModelo, on_delete=models.CASCADE, null=False)
    consulta_id = models.ForeignKey(ConsultaModelo, on_delete=models.CASCADE, null=False)
    enfermedad_id = models.ForeignKey(EnfermedadModelo, on_delete=models.CASCADE, null=False)
    
    
    class Meta:
        db_table = 'diagnostico'



class FacturaModelo(models.Model):
    costo = models.FloatField() 
    fecha = models.DateTimeField(default=timezone.now)
    motivo = models.CharField(max_length=250, null=False)   
    pago_id = models.ForeignKey(PagosModelo, on_delete=models.CASCADE, null=False)
    consulta_id = models.ForeignKey(ConsultaModelo, on_delete=models.CASCADE, null=False)
    paciente_id = models.ForeignKey(PacienteModelo, on_delete=models.CASCADE, null=False)
    

    class Meta:
        db_table = 'factura'







