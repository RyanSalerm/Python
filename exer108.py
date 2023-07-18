"""Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado."""
import moedas2
numero = int(input('Digite um valor: '))
aumento = int(input('Aumento: '))
diminuir = int(input('Diminuir: '))
numeros = moedas2.moeda(numero)
aumentos = moedas2.moeda(aumento)
diminuirs = moedas2.moeda(diminuir)
print(f'Aumentando R$ {numeros} em {aumentos}% é {moedas2.moeda(moedas2.aumentar(numero, aumento))}')
print(f'Diminuindo R$ {numeros} em {diminuirs}% é {moedas2.moeda(moedas2.diminuir(numero, diminuir))}')
print(f'O dobro de R${numeros} é {moedas2.moeda(moedas2.dobro(numero))}')
print(f'A metade de R${numeros} é {moedas2.moeda(moedas2.metade(numero))}')

