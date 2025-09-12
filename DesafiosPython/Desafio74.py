lista = list()

escolha = 'S'
while escolha == 'S':
    lista.append(int(input('Digite um valor: ')))
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    if escolha == 'N':
        break

print('=' + '-=' *20)
print(f'A lista tem {len(lista)} valores.')
print(f'A lista ordenada em valores decrescente:\n{sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')