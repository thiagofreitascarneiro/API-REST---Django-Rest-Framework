from rest_framework import serializers

from .models import Curso, Avaliacao


class AvalizacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kargs = {
            'email': {'write_only': True}
        }
        models = Avaliacao 
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )