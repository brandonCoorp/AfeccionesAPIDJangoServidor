from dataclasses import fields
from rest_framework import serializers
from .models import PacienteModelo, ConsultaModelo, DiagnosticoModelo
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteModelo
        fields = ['id','nombre', 'email','password']

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaModelo
        fields = ('id','imagen', 'estado','paciente_id')

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticoModelo
        fields = ('id','resultado','imagen', 'consulta_id','enfermedad_id','paciente_id')
