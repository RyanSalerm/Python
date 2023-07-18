'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador_de_futebol = dict()
print("Cadrastrando um jogador de futebol\n")
jogador_de_futebol['Nome'] = str(input('Nome: '))
jogador_de_futebol['Partidas'] = int(input('Número de partidas: '))
n = jogador_de_futebol['Partidas'] + 1
lista = []
jogador_de_futebol['Gols'] = lista
print("\n")
for c in list(range(1, n)):
               lista.append(int(input(f'Partida {c}.Gols: ')))
               soma=0
               for numero in lista:
                   soma+=numero
print("\n")               
for c, k in enumerate(lista):
              print(f'Na partida {c}, fez {k} gols')
jogador_de_futebol['Total'] = soma
print("\n")
for k, v in jogador_de_futebol.items():
    print(f'{k}: {v}')



