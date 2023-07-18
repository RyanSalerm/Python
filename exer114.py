from urllib.request import urlopen
from urllib.error import URLError
def site(acessivel):
    try:
        urlopen(acessivel)
        print('O site está acessível')
    except URLError as erro:
        print(f'O site não está acessível. Erro: {erro}')
site("http://pudim.com.br/")