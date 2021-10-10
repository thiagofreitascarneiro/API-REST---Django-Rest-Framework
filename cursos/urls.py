from django.urls import path 

from .views import CursoAPIView, AvalizacaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvalizacaoAPIView.as_view(), name='avaliacoes'),
]