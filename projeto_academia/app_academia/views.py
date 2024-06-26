from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Treino
from .models import Aluno
from .models import Maquina


def treinos(request):

    if request.method == 'POST':
        novo_treino = Treino()
        novo_treino.aluno_id = request.POST.get('aluno')
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

def maquinas(request):
    nova_maquina = Maquina()
    nova_maquina.nome = request.POST.get('nome')
    nova_maquina.grupo_muscular = request.POST.get('grupo_muscular')
    nova_maquina.marca = request.POST.get('marca') 
    nova_maquina.data_compra = request.POST.get('data_compra')
    nova_maquina.ult_manutencao = request.POST.get('ult_manutencao')
    nova_maquina.fornecedor = request.POST.get('fornecedor')
    nova_maquina.prazo_manutencao = request.POST.get('prazo_manutencao')
    nova_maquina.prox_manutencao = request.POST.get('prox_manutencao')
    nova_maquina.responsavel = request.POST.get('responsavel')
    nova_maquina.garantia = request.POST.get('garantia')
    nova_maquina.unidade = request.POST.get('unidade')
    nova_maquina.save()

    maquinas = {
        'maquinas': Maquina.objects.all()
    }

    return render(request, 'telaGerente/listaMaquinario.html', maquinas)

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

def listaMaquinario(request):
    return render(request, 'telaGerente/listaMaquinario.html')

def telaRecepcionista(request):
    return render(request, 'telaRecepcionista/telaRecepcionista.html')

def listaAluno(request):
    alunos = {
        'alunos': Aluno.objects.all()
    }
    return render(request, 'telaRecepcionista/listaAluno.html', alunos)

def cadAluno(request):
    return render(request, 'telaRecepcionista/cadAluno.html')

def delete(request, cpf):
    aluno = Aluno.objects.get(cpf=cpf)
    aluno.delete()
    alunos = {
        'alunos': Aluno.objects.all()
    }
    return render(request, 'telaRecepcionista/listaAluno.html', alunos)


def homeAluno(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')  # Obtenha a matrícula do formulário
        # Verifique se a matrícula corresponde a algum aluno no banco de dados
        if Aluno.objects.filter(cpf=matricula).exists():
            # Se a matrícula (CPF) existe no banco de dados, renderize a página 'homeAluno'
            return render(request, 'telaAluno/homeAluno.html')
        else:
            # Se a matrícula (CPF) não existe no banco de dados, exiba uma mensagem de aviso
            return HttpResponse("Aluno não cadastrado")
    else:
        # Se o método HTTP não for POST, retorne um HttpResponse vazio ou renderize uma página de erro
        return HttpResponse("Método não permitido")

