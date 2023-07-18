'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos
os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(*numeros):
    maior = cont = 0
    print('Analisando os valores passados...\n')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo\n')
    print(f'O maior valor informado foi {maior}.')
maior(2, 9, 4, 5, 7, 1)
          
          
"""         
from random import randint
numeros = list()
def maior(começo, fim):
    quant_valor = randint(começo, fim)
    cont=0
    while cont < quant_valor:
        numeros.append(randint(começo, fim))
        cont+=1
    print('Analisando os valores sorteados...\n')
    print(f'{ numeros }. Foram informados {cont} valores ao todo')
    print(f'O maior deles foi {max(numeros)}')
    print(f'{"-="*25}')
começo = int(input('Começo: '))
fim = int(input('Fim: '))
maior(começo, fim)"""
