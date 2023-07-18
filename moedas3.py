"""Exercício Python 109: Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando se o valor retornado
por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
def moeda(int=0):
    return f'R${int:.2f}'.replace('.',',')


def aumentar(int=0, por=0, sit=False):
    porc = 1+(por/100)
    aumento = int*porc
    if sit == True:
        return f'R${aumento:.2f}'
    else:
        return aumento


def diminuir(int=0, por=0, sit=False):
    porc = 1-(por/100)
    diminuir = int*porc
    if sit==True:
        return f'R${diminuir:.2f}'
    else:
        return diminuir
    
    
def dobro(int=0, sit=False):
    vezesdois = int*2
    if sit==True:
        return f'R${vezesdois:.2f}'
    else:
        return vezesdois


def metade(int=0, sit=False):
    vezesdois = int/2
    if sit==True:
        return f'R${vezesdois:.2f}'
    else:
        return vezesdois



def resumo(p, aum, dim):
    print('-'*31)
    print(f'{" "*7}Resumo do Valor{" "*7}')
    print('-'*31)
    print(f'Preço Analisado: {moeda(p):>14}')
    print(f'Dobro do preço: {moeda(dobro(p)):>15}')
    print(f'Metade do preço: {moeda(metade(p)):>14}')
    print(f'{aum}% de aumento: {moeda(aumentar(p, aum, False)):>15}')
    print(f'{dim}% de redução: {moeda(diminuir(p, dim, False)):>15}')
    
    
    
    
    