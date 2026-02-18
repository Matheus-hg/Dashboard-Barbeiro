from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

def produtos(request):
    # Cadastro
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("produtos")
    else:
        form = ProdutoForm()

    # Listagem
    produtos = Produto.objects.all()

    return render(request, "produtos/produtos.html", {
        "form": form,
        "produtos": produtos
    })

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("produtos")
    else:
        form = ProdutoForm(instance=produto)

    produtos = Produto.objects.all()
    return render(request, "produtos/produtos.html", {
        "form": form,
        "produtos": produtos,
        "produto_editando": produto
    })

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect("produtos")
