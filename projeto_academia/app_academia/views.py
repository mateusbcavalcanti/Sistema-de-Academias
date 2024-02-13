from django.shortcuts import render
from .models import Treino

def telaProf(request):
    return render(request, 'telaProf/telaProf.html')

def treinos(request):
    if request.method == 'POST':
        novo_treino = Treino()
        novo_treino.aluno = request.POST.get('aluno')
        novo_treino.treino = request.POST.get('treino')
        novo_treino.save()

    treinos = {
        'treinos': Treino.objects.all()
    }

    return render(request, 'telaProf/treinos.html', treinos)
