'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas
funções.'''
import moedas
numero = int(input('Digite um valor: '))
aumento = int(input('Aumento: '))
diminuir = int(input('Diminuir: '))
moedas.aumentar(numero, aumento )
moedas.diminuir(numero, diminuir)
moedas.dobro(numero)
moedas.metade(numero)