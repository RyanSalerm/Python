'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a área do terreno.'''
def area(largura, comprimento):
    area = largura * comprimento
    print(f'As dimensões do terreno são {largura}x{comprimento}.')
    print(f'Área: {area}m2')


print('Controle de terreos')
print('-'*20)
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))
area(largura, comprimento)
    