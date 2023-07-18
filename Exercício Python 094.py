'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de
idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
'''
#criou uma lista e um dicionario
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).upper() #colocar em maiusculo, para ficar mais organizado
    
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MmfF' and not pessoa['Sexo'].isnumeric():
            break
        print('Por favor. Digite novamente M ou F. ')
       
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
        
    continuar = str(input('Deseja continuar [S/N]: '))
    print('\n')
    galera.append(pessoa.copy())
    if continuar in 'Nn':
        break
print(f'A) São {len(galera)} pessoas cadrastadas')
print(f'B) Média: {soma/len(galera)}')
print(f'C) As mulheres cadrastadas foram ', end='')
for p in galera:
    if p['Sexo'] in 'fF':
        print(f'{p["nome"]},  ', end='')
print()

print('A lista de pessoas acima da média foram ', end='')
media = soma/len(galera)
for p in galera:
    if p['Idade'] >= media:
        print(f'D) {p["nome"]},  ', end='')
print()
    