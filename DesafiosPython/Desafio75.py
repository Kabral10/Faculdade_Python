lista = list()
listapar = list()
listaimpar = list()

escolha = 'S'
while escolha == 'S':
    numero = (int(input('Digite um valor: ')))
    lista.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)

    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    if escolha == 'N':
        break
print('=' + '-=' *20)
print(f'A lista contem os valores:\n{lista}')
print(f'A lista de numeros pares contem os valores:\n{listapar}')
print(f'A lista de impares contem os valores:\n{listaimpar}')
