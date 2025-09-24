#Passo1 -> Definir e importar
def notas(*valores, sit=False):
    """
    -> Função para analisar notas
    :param valores: Uma ou mais notas
    :param sit: Mostra a situacao do aluno [Aprovado ou reprovado]
    :return: Dicionario com as informações da turma
    """
    dicionario = {}
    dicionario['Quantidade'] = len(valores)
    dicionario['Maior'] = max(valores)
    dicionario['Menor'] = min(valores)
    dicionario['Media'] = sum(valores) / len(valores)

    if sit:
        if dicionario['Media'] >= 70:
            dicionario['situacao'] = 'Aprovado'
        else:
            dicionario['situacao'] = 'Reprovado'

    return dicionario

resposta = notas(40, 50, 90, sit=True)
print(resposta)