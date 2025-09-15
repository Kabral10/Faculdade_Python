from datetime import date

Dados = dict()

#Criação de dados
Dados['Nome'] = str(input('Nome: ')).title().strip()
Dados['Ano de nascimento'] = int(input('Ano de nascimento: '))
Dados['CTPS'] = int(input('CTPS: '))
Dados['Idade'] = date.today().year - Dados['Ano de nascimento']

if Dados['CTPS'] != 0:
    Dados['Ano de Contratação'] = int(input('Quando foi contratado: '))
    Dados['Salario'] = float(input('Salario: '))
    Dados['Aposentadoria'] = Dados['Ano de Contratação'] + 35

print('=-'*15+'=')
print(Dados)
print('=-'*15+'=')
for k, v in Dados.items():
    print(f'{k}: {v}')