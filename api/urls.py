from django.urls import path
from .views import PagoView
from .Controlador.diagnosticar import Diagnosticar
from .Controlador.administrador import AdministradorControl
from .Controlador.paciente import PacienteControl, LoginControl, LogoutControl, UserView
from .Controlador.pagos import PagoControl
from .Controlador.aplicacion import AplicacionControl
from .Controlador.enfermedad import EnfermedadControl
from .Controlador.consulta import ConsultaControl, UploadImagen
from .Controlador.diagnostico import DiagnosticoControl
from .Controlador.factura import FacturaControl


urlpatterns = [
    #url administrador 
    path('administrador/', AdministradorControl.as_view(), name='verAdministrador' ),
    path('administrador/<int:id>', AdministradorControl.as_view(), name='actualizarAdministrador' ),

    #url pacientes 
    path('pacientes/', PacienteControl.as_view(), name='listarPacientes' ),
    path('pacientes/<int:id>', PacienteControl.as_view(), name='modificarPaciente' ),
    path('login/',LoginControl.as_view(), name='loginPaciente' ),
    path('logout/',LogoutControl.as_view(), name='logoutPaciente' ),
    path('viewPaciente/',UserView.as_view(), name='verPaciente' ),
    

    #url aplicacion 
    path('aplicacion/', AplicacionControl.as_view(), name='verAplicacion' ),
    path('aplicacion/<int:id>', AplicacionControl.as_view(), name='actualizarAplicacion' ),

    #url pagos 
    path('Pagos/', PagoControl.as_view(), name='listarPagos' ),
    path('Pagos/<int:id>', PagoControl.as_view(), name='modificarPago' ),

    #url enfermedad 
    path('enfermedad/', EnfermedadControl.as_view(), name='listarenfermedad' ),
    path('enfermedad/<int:id>', EnfermedadControl.as_view(), name='modificarEnfermedad' ),
     path('enfermedadN/<str:nombre>', EnfermedadControl.getbyNombre, name='enfermedadbynombre' ), 

    #url consulta 
    path('consulta/', ConsultaControl.as_view(), name='listarConsulta' ),
    path('consulta/<int:id>', ConsultaControl.as_view(), name='verConsulta' ),
    path('crearconsulta/', UploadImagen.as_view(), name='CrearConsulta' ),

    #url diagnostico 
    path('diagnostico/', DiagnosticoControl.as_view(), name='listarDiagnostico' ),
    path('diagnostico/<int:id>', DiagnosticoControl.as_view(), name='verDiagnostico' ),
    path('DiagnosticoUser/<int:id>', DiagnosticoControl.obtenerDiagnosticoUser, name='diagnosticoUser' ), 

    #url factura 
    path('factura/', FacturaControl.as_view(), name='listarFactura' ),
    path('factura/<int:id>', FacturaControl.as_view(), name='verDactura' ),

    #diagnosticarEnfermedad
    path('Diagnosticar/', Diagnosticar.as_view(), name='Diagnosticar' ), 
    path('Diagnosticar/saludar', Diagnosticar.Saludar, name='saludar' ), 

   
]
