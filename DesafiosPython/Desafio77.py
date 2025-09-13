pessoas = list()
dados = list()

escolha = 'S'

while escolha == 'S':
    print('Cadastrar uma pessoa')
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    escolha = input('Deseja continuar? [S/N]').strip().upper()
    if escolha == 'N':
        break
print('='+'-='*20)
print(f'O total de pessoas cadastradas é: {len(pessoas)}')

mais_pesada = pessoas[0]
mais_leve = pessoas[0]

for pessoa in pessoas[1:]:
    if pessoa[1] > mais_pesada[1]:
        mais_pesada = pessoa
    if pessoa[1] < mais_leve[1]:
        mais_leve = pessoa

print(f'A pessoa mais pesada é {mais_pesada[0]} com {mais_pesada[1]}Kg')
print(f'A pessoa mais leve é {mais_leve[0]} com {mais_leve[1]}Kg')

