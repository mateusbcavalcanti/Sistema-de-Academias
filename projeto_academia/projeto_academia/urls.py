from django.urls import path
from app_academia import views

urlpatterns = [
    path('telaProf/', views.telaProf, name='telaProf'),
    path('treinos/', views.treinos, name='listagem_treinos')
]
