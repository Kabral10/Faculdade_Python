lista = list()
escolha = 'S'

while escolha == 'S':
    numero = (int(input('Digite um numero: ')))
    if numero not in lista:
        lista.append(numero)
        print(f'{numero} adicionado a lista com sucesso')
    elif numero in lista:
        print(f'{numero} já existe na lista!')

    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    if escolha == 'N':
        break

print(f'A lista é:\n{sorted(lista)}')