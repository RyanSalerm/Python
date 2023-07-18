'''Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''
def notas(*txt, sit=False):
    """
    -----------------------
    Help on function notas in module __main__:
    notas(*txt, sit=False):
        :Funções para analisar as notas e situação de vários alunos.
        :param txt: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não indicar a situação
        :return: dicionário com várias informações sobre a situação da turma
    """
    valores = dict()
    cont = len(txt)
    valores['Quantidade'] = cont
    valores['Maior'] = max(txt)
    valores['Menor'] = min(txt)
    valores['Média'] = sum(txt)/cont
    if sit == True:
        if valores['Média'] >= 7:
            valores['Situação'] = "Boa"
        elif valores['Média'] >= 5:
            valores['Situação'] = "Razoável"
        else:
            valores['Situação'] = "Ruim"
    return valores
resp = notas(7, 7, 7, sit=True)
print(resp)
help(notas)        
    
    
