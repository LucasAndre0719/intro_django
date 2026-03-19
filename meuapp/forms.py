from django import forms
from .models import pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = pessoa
        fields = ['nome', 'idade', 'email', 'telefone']
