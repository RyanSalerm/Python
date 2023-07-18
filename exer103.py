"""Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
jogador = str(input('Nome do jogador: '))
gols = str(input('Gols: '))
def ficha(jogador, gols):
    if jogador == "" and gols == "":
        return print(f'O jogador <desconhecido> fez 0 gols(s) no campeonato.')
    elif jogador == "":
        return print(f'O jogador <desconhecido> fez {gols} gols(s) no campeonato.')
    else:
        return print(f'O jogador {jogador} fez {gols} gols(s) no campeonato.')
ficha(jogador, gols)
