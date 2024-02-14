from django.urls import path
from app_academia import views

urlpatterns = [
    # Rota, view responsável, nome de referência
    path('', views.home, name= 'home'),
    path('telaProf/', views.telaProf, name='telaProf'),
    path('treinos/', views.treinos, name='listagem_treinos'),
    path('telaAluno/', views.telaAluno, name='telaAluno')
]
