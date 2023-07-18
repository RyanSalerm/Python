'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.'''
from datetime import date
atual = date.today().year
def voto(ano):
    idade = atual - ano
    print(f'Com {idade} anos é: ', end='')
    if idade >= 18 and idade <= 70:
        return print('VOTO OBRIGATÓRIO')
    elif idade > 16 and idade < 18 or idade > 70:
        return print('VOTO OPCIONAL')
    else:
        return print('VOTO NEGADO')
nascimento = int(input('Ano de nascimento: '))
voto(nascimento)