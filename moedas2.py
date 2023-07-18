"""Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado."""
def aumentar(int=0, por=0):
    porc = 1+(por/100)
    aumento = int*porc
    return aumento
    
    
def diminuir(int=0, por=0):
    porc = 1-(por/100)
    diminuir = int*porc
    return diminuir
    
    
def dobro(int=0):
    return int*2


def metade(int=0):
    return int/2


def moeda(int=0):
    return f'R${int:.2f}'