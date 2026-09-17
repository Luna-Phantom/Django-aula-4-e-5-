from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all()

    # Captura parâmetros via GET
    nome = request.GET.get('nome')
    tipo = request.GET.get('tipo')
    categoria = request.GET.get('categoria')

    # Aplica os filtros solicitados
    if nome:
        livros = livros.filter(titulo__icontains=nome)
    if tipo:
        livros = livros.filter(tipo=tipo)
    if categoria:
        livros = livros.filter(categoria=categoria)

    contexto = {
        'livros': livros,
        'tipos': Livro.TIPO_CHOICES,
        'categorias': Livro.CATEGORIA_CHOICES,
        'filtros': {
            'nome': nome or '',
            'tipo': tipo or '',
            'categoria': categoria or '',
        }
    }
    return render(request, 'acervo/lista.html', contexto)

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})