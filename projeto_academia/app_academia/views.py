from django.shortcuts import render, redirect
from .models import Treino
from .models import Aluno


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


def alunos(request):
    # salvando as informações a tela no banco
    novo_aluno = Aluno()
    novo_aluno.cpf = request.POST.get('CPF')
    novo_aluno.nome = request.POST.get('nome')
    novo_aluno.data_nasc = request.POST.get('data')
    novo_aluno.telefone = request.POST.get('telefone')
    novo_aluno.pacote = request.POST.get('pacote')
    novo_aluno.save()

    # exibindo todos os usuários cadastrados em nova tela
    alunos = {
        'alunos': Aluno.objects.all()
    }

    # retornando os dados para a página de listagem dos alunos
    return render(request, 'telaRecepcionista/listaAluno.html', alunos)


def home(request):
    return render(request, 'usuarios/home.html')


def telaAluno(request):
    return render(request, 'telaAluno/loginAluno.html')


def telaProf(request):
    return render(request, 'telaProf/telaProf.html')


def telaGerente(request):
    return render(request, 'telaGerente/telaGerente.html')


def cadMaquinario(request):
    return render(request, 'telaGerente/cadMaquinario.html')


def telaRecepcionista(request):
    return render(request, 'telaRecepcionista/telaRecepcionista.html')


def listaAluno(request):
    return render(request, 'telaRecepcionista/listaAluno.html')


def cadAluno(request):
    return render(request, 'telaRecepcionista/cadAluno.html')


def delete(request, cpf):
    aluno = Aluno.objects.get(cpf=cpf)
    aluno.delete()
    return redirect("")
