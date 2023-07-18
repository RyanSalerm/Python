'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento de cada jogador.

Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

vai fazer um dicionário para cada jogador que será adicionado numa lista. *Depois mostrar dados de qual jogador?* que mostra que na
partida 1 fez tantos gols'''
elenco = list() #tudo copiado para cá
jogador_de_futebol = dict() #nomes e gols(lista)
lista = list()  #golsfor k,v in enumerate(elenco):
while True:
    jogador_de_futebol.clear()
    print("Cadrastrando um jogador de futebol\n")
    jogador_de_futebol['Nome'] = str(input('Nome: '))
    tot= int(input('Número de partidas: '))
    lista.clear()
    n = tot + 1
    jogador_de_futebol['Gols'] = lista
    print("\n")
    for c in list(range(1, n)):
        lista.append(int(input(f'Partida {c}.Gols: ')))
        soma=0
    jogador_de_futebol['Gols'] = lista[:]    
    jogador_de_futebol['Total'] = sum(lista)
    elenco.append(jogador_de_futebol.copy())
    while True:
        continuar = str(input('\nDeseja cadrastrar mais um jogador?[S/N]: ')).upper().strip()[0]
        if continuar in 'SnNn':
            break
        print('Erro digite novamente')
    if continuar in 'Nn':
        break
    print("\n")
print('-'*40)
print('cod ', end=' ')
for i in jogador_de_futebol.keys():
    print(f'{i:<15}', end=' ')
print()
print('-'*40)
for k, v in enumerate(elenco):
    print(f'{k:>3}', end= ' ')
    for d in v. values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(elenco):
        print(f'Não existe jogador com o código {busca}')
    else:
        print('Levatamento do jogador{elenco[busca]["Nome"]}:')
        for i, g in enumerate(elenco[busca]["Gols"]):
            print(f'  No jogo {i+1} fez {g} gols')
        print('-'*40)
                               
