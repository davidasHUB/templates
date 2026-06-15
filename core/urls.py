
from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio,name="inicio"),

    path('curso_galeria/',curso_galeria,name="curso_galeria"),
    path('contato/',contato,name="contato"),
    path('login/',login,name="login"),
    #path('perfil/',perfil,name="perfil"),
    path('curso_detalhe/',curso_detalhe,name="curso_detalhe"),
    path('cadastro/',cadastro,name="cadastro"),
    path('atividade/',inicio,name="atividade"),
    
    path('areas/', areas,name="area_listar"),
    
    path('area_cadastrar/',area_cadastrar,name='area_cadastrar'),
    path('area_editar/<int:id>/',area_editar,name='area_editar'),
    path('area_remover/<int:id>/',area_remover,name='area_remover'),

    path('publicoalvo/', publico_alvo,name="publicoalvo"),

    path('publico_cadastrar/',publico_alvo_cadastrar,name='publico_cadastrar'),

    path('publico_editar/<int:id>/',publico_alvo_editar,name='publico_editar'),
    path('publico_remover/<int:id>/',publico_alvo_remover,name='publico_remover'),
    
    path('cursos/', curso_listar,name="cursos"),
    path('curso_cadastrar/',curso_cadastrar,name='curso_cadastrar')

]
