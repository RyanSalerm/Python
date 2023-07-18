'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * -1
    if passo < 0:
        print(f'\n\nContagem de {inicio} até {fim}, voltando de {passo*-1} em {passo*-1}')
    elif passo == 0:
        passo = 1
        print(f'\n\nContagem de {inicio} até {fim}, voltando de {passo} em {passo}')
    else:
        print(f'\n\nContagem de {inicio} até {fim}, voltando de {passo} em {passo}')
    print(f'{inicio}', end='')
    if fim > inicio:
        while(inicio < fim):
            sleep(0.5)
            inicio+=passo
            print(f'   {inicio}', end='')
    else:
        while(fim  < inicio):
            sleep(0.5)
            inicio-=passo
            print(f'  {inicio}', end='')

Inicio = 1
Fim = 10
Passo = 1
contador(Inicio, Fim, Passo)

Inicio = 10
Fim = 1
Passo = 2
contador(Inicio, Fim, Passo)

print('\n\nContagem Personalizada')
Inicio = int(input("Inicio: "))
Fim = int(input('Fim: '))
Passo = int(input('Passo: '))
print('-'*40)
contador(Inicio, Fim, Passo)
