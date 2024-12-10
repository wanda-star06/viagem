from django.shortcuts import render, get_object_or_404, redirect
from .models import Destino, Pacote
from .forms import DestinoForm, PacoteForm
from django.shortcuts import render

def tela_inicial(request):
    return render(request, 'gerenciamento_viagem/tela_inicial.html')

def lista_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'gerenciamento_viagem/destino_lista.html', {'destinos': destinos})

def cria_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinoForm()
    return render(request, 'gerenciamento_viagem/destino_form.html', {'form': form})

def edita_destino(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if request.method == 'POST':
        form = DestinoForm(request.POST, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'gerenciamento_viagem/destino_form.html', {'form': form})

def deleta_destino(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if request.method == 'POST':
        destino.delete()
        return redirect('lista_destinos')
    return render(request, 'gerenciamento_viagem/destino_confirm_delete.html', {'destino': destino})


def lista_pacotes(request):
    pacotes = Pacote.objects.all()
    return render(request, 'gerenciamento_viagem/pacote_lista.html', {'pacotes': pacotes})

def cria_pacote(request):
    if request.method == 'POST':
        form = PacoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacotes')
    else:
        form = PacoteForm()
    return render(request, 'gerenciamento_viagem/pacote_form.html', {'form': form})

def edita_pacote(request, pk):
    pacote = get_object_or_404(Pacote, pk=pk)
    if request.method == 'POST':
        form = PacoteForm(request.POST, instance=pacote)
        if form.is_valid():
            form.save()
            return redirect('lista_pacotes')
    else:
        form = PacoteForm(instance=pacote)
    return render(request, 'gerenciamento_viagem/pacote_form.html', {'form': form})

def deleta_pacote(request, pk):
    pacote = get_object_or_404(Pacote, pk=pk)
    if request.method == 'POST':
        pacote.delete()
        return redirect('lista_pacotes')
    return render(request, 'gerenciamento_viagem/pacote_confirm_delete.html', {'pacote': pacote})
