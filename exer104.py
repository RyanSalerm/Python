'''Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''
def leiaInt(txt):
    valor = input(txt)
    while not valor.isnumeric():
        print('\033[0;31;1mERRO\033[m')
        valor = input('Digite um número: ')
    return valor
    
    
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')