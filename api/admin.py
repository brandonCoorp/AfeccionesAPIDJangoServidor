import django
from django.contrib import admin
from .models import DiagnosticoModelo, EnfermedadModelo, PacienteModelo, PagosModelo, AplicaciónModelo
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(AplicaciónModelo)
admin.site.register(EnfermedadModelo)


class PacienteAdminConfig(UserAdmin):
    search_fields = ('email', 'nombre', 'apellido',)
    list_filter = ('email', 'nombre', 'apellido', 'is_active',)
    ordering = ('-nombre',)
    list_display = ('email','user_name','nombre','apellido', 'is_active', 'is_staff',)

    fieldsets = (
        (None, {'fields':('email', 'user_name',)}),
        ('Permisos',{'fields':('is_active', 'is_staff',)}),
        ('Personal',{'fields':('nombre','apellido','edad','sexo',)}),
    )


    add_fieldsets = (
        (None, {'fields':('email', 'user_name', 'password1', 'password2', )}),
        ('Permisos',{'fields':('is_active', 'is_staff',)}),
        ('Personal',{'fields':('nombre','apellido','edad','sexo',)}),
    )

   

admin.site.register(PacienteModelo, PacienteAdminConfig)
admin.site.register(PagosModelo)
admin.site.register(DiagnosticoModelo)
