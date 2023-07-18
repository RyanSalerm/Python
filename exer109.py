"""Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que
elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108."""
import moedas3
numero = int(input('Digite um valor: '))
aumento = int(input('Aumento: '))
diminuir = int(input('Diminuir: '))
newnumber = moedas3.moeda(numero)
print(f'Aumentando {newnumber} em {aumento}% é {moedas3.aumentar(numero, aumento, sit=True)}')
print(f'Diminuindo {newnumber} em {diminuir}% é {moedas3.diminuir(numero, diminuir, sit=True)}')
print(f'O dobro de {newnumber} é {moedas3.dobro(numero, sit=True)}')
print(f'A metade de {newnumber} é {moedas3.metade(numero, sit=True)}')