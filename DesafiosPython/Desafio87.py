lista = list()
mulheres = list()
dados = dict()


escolha = 'S'
while escolha == 'S':
    dados['nome'] = input('Nome: ').title().strip()
    dados['sexo'] = input('Sexo (M/F): ').upper().strip()
    dados['idade'] = int(input('Idade: '))

    lista.append(dados.copy())

    if dados['sexo'] == 'F':
        mulheres.append(dados.copy())

    dados.clear()

    escolha = input('Deseja continuar? [S/N]: ').upper().strip()

print('=-'*15+'=')
print(f'O total de cadastros foi: {len(lista)}')

#media de idades
media = sum(p['idade'] for p in lista) / len(lista)
print(f'A média de idade do grupo é: {media:.1f}')

print(f'Aqui estão todas as mulheres:')
for m in mulheres:
    print(f' -> {m["nome"]}: {m["idade"]}')

print(f'As pessoas com a idade acima da media são:')
for p in lista:
    if p['idade'] > media:
        print(f' -> {p["nome"]}: {p["idade"]}')
