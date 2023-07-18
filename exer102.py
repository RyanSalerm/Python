'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def fatorial(n, show=False):
    """
    ------------------------------
    Help on function fatorial in module __main__:
    
    fatorial(n, show=False)
        -> Calcula um faotrial de um número
        :parâmetro n: O número a ser cálculado
        :parâmetro show: (opcional) Mostrar ou não a conta.
        :return: O valor do fatorial de um número n.
    """
    f=1
    for c in range(n, 0, -1):
        f *= c
    if show == True:
        contador=0
        while contador<=n:
            if (n-contador)==1:
                print(f'1 = {f}')
                break
            print(f'{n-contador} x ', end='')
            contador+=1
    else:
        return print(f'{f}')
numero = int(input('Número: '))
fatorial(numero, show=True)
fatorial(numero)
help(fatorial)
