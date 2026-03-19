from django.test import TestCase
import requests

cep = "58036460"

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

dados = resposta.json()

print(dados)

# Create your tests here.
