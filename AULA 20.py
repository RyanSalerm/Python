#AULA20
#ANTES:
'''a = 1
b = 2
c = a + b
print(c)

a = 3
b = 4
c = a + b
print(c)

a = 5
b = 6
c = a + b
print(c)

#DEPOIS:
def soma(a, b):
    s = a + b
    print(s)
    

#programa principal (deixe duas linhas de diferença da função)
soma(1, 2)
soma(3, 4)
soma(5, 6)'''


'''
def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f"A soma é A + B = {s}")
soma(b=4, a=5)
soma(a=4, b=5)'''

#empacotar parâmetros
'''
def contador(*núm):
    s=0
    for valor in núm:
        s+=valor
        print(f"Somando os {núm} temos {s}")
   
   ou
    
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')

contador(2, 4, 7)
contador(1, 3)
contador(7, 5, 6, 2)'''

#listas
'''valores = [7,2,5,0,4]
dobra(valores)
print(valores)'''

"""def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1
valores = [7,2,5,0,4]
dobra(valores)
print(valores)"""


















