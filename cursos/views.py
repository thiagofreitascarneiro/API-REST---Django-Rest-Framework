from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer



class CursoAPIView(APIView):
    '''
    API de cursos
    '''

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AvalizacaoAPIView(APIView):
    '''
    API de Avaliações 
    '''
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)