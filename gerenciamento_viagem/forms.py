from django import forms
from .models import Destino, Pacote

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class PacoteForm(forms.ModelForm):
    class Meta:
        model = Pacote
        fields = '__all__'
