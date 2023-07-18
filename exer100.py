"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior."""
valores = list()
from random import randint
inicio = 0
fim = 10
def sorteia(inicio, fim):
    contador = 0
    while contador < 5:
        valores.append(randint(inicio, fim))
        contador+=1
    print(f'Sorteando 5 valores da lista: { valores } PRONTO!')
def somaPAR(valores):
    soma = sum([x for x in valores if x % 2 == 0])
    print(f'Somando os valores pares de { valores }, temos {soma}')
sorteia(inicio, fim)
somaPAR(valores)