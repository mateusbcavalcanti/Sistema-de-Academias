from django.urls import path
from app_academia import views
from django.contrib import admin

urlpatterns = [
    # Rota, view responsável, nome de referência
    path('', views.home, name='home'),
    path('telaAluno/', views.telaAluno, name='telaAluno'),
    path('telaProf/', views.telaProf, name='telaProf'),
    path('treinos/', views.treinos, name='listagem_treinos'),
    path('telaGerente/', views.telaGerente, name='telaGerente'),
    path('telaRecepcionista/', views.telaRecepcionista, name='telaRecepcionista'),
    path('listaAlunos/', views.listaAlunos, name='listaAlunos')
]
