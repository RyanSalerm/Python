'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas
funções.'''
def aumentar(int, por):
    porc = 1+(por/100)
    aumento = int*porc
    print(f'Aumentando em {por}%, temos R${aumento:.2f}.')
    
    
def diminuir(int, por):
    porc = 1-(por/100)
    diminuir = int*porc
    print(f'Diminuindo em {por}%, tenos R${diminuir:.2f}')
    
    
def dobro(int):
    return print(f'Dobro: {int*2}')


def metade(int):
    return print(f'Metade: {int/2}')

