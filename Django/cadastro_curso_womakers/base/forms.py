from django import forms  #importa funcionalidade próprio do django
from base.models import Cadastro

# classe principal
class CadastroForm(forms.ModelForm): # modelo ModelForm
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
