'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer 
como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~'''
def escreva(txt):
    quant_laços = len(txt)
    print('\n')
    print(f'~~{"~"*quant_laços}~~')
    print(f'  {txt}  ')
    print(f'~~{"~"*quant_laços}~~')
texto = str(input('Digite um texto: '))
escreva(f'{texto}')