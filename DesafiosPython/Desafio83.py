situacao = dict()

situacao['Nome'] = str(input('Nome: ')).title().strip()
situacao['Media'] = float(input('Qual foi sua media: '))

if situacao['Media'] >= 7:
    situacao['Situacao'] = 'Aprovado'
else:
    situacao['Situacao'] = 'Reprovado'

print(f'Aluno: {situacao['Nome']}')
print(f'Sua media é: {situacao['Media']}')
print(f'Você está: {situacao['Situacao']}')
