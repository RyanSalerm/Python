'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaint(txt):
    while True:
        try:
            valor = int(input(txt))
            return valor
        except Exception as erro:
            print(f'\033[0;31;1mERRO: {erro.__class__}\033[m')
        else:
            valor = int(input('Digite um número inteiro: '))



def leiafloat(txt):
    while True:
        try:
            valot = float(input(txt))
            return valot
        except Exception as erro:
            print(f'\033[0;31;1mERRO: {erro.__class__}\033[m')
        else:
            valot = float(input('Digite um número real: '))
 
 
 
valores = leiaint('Número Inteiro: ')
print(f'Você digitou o número {valores}')
valott = leiafloat('Número Real: ')
print(f'Você digitou o número {valott}')
