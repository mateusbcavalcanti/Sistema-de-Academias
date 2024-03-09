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
    path('cadMaquinario/', views.cadMaquinario, name='cadMaquinario'),
    path('telaRecepcionista/', views.telaRecepcionista, name='telaRecepcionista'),
    path('cadAluno/', views.cadAluno, name='cadAluno'),
    path('listaAluno/', views.alunos, name='listagem_alunos'),
    path('delete/<str:cpf>', views.delete, name='delete')
]
