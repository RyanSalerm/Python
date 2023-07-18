'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
from time import sleep
def helpPy():
   while True:
    print('\n\033[0;31;1m~~~Sistema de ajuda PyHELP~~~\033[m')
    txt = str(input('Função ou biblioteca: ')).lower().strip()
    if 'fim' not in txt:
        print(f'\n\033[0;31;1m~~~Acessando Manual do comando {txt}~~~\033[m')
        sleep(1)
        help(txt)
    else:
        print('\n\033[0;31;1m~~ATÉ LOGO~~\033[m')
        break
helpPy()
