from django.shortcuts import render
from passagens.forms import PassagemForm


def index(request):
    """
    Renderiza pagina principal
    """
    form = PassagemForm()
    contexto = {
        'form': form
    }
    return render(request, 'index.html', contexto)


def revisao_consulta(request):
    """
    Consiste dados cadastrados e renderiza tela de consulta
    """
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        contexto = {
            'form': form
        }
    return render(request, 'minha_consulta.html', contexto)
