"""Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), 
mas com uma validação de dados para aceitar apenas valores que seja monetários.

leia dinheiro:
	Se digitar 30.05 ou 30,05 ele funciona
	Informa que está errado se:
		se digitar uma palavra, exemplo "barato"
		se não digitar nada
		se informar vários espaços "    baratp"
moeda.resumo(p, 35, 22)"""
def leiadinheiro(txt):
    valor = str(input(txt)).strip().replace(',','.')
    while valor.isalpha() or valor == "":
        print(f"\033[0;31;1mErro: '{valor}' é um preço inválido\033[m")
        valor = str(input(txt)).strip().replace(',','.')
    return float(valor)



    
