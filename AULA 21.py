'''def fatorial(n = 1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
'''


'''
f1 = fatorial(1)
f2 = fatorial(5)
f3 = fatorial(2)
'''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('É impar')
