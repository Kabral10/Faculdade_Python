print('=-=-=-=-=-=-=')
print('| Banco LMC |')
print('=-=-=-=-=-=-=')

while True:
    valor = int(input('Quanto deseja sacar? R$'))

    if valor < 0:
        break

    N50 = valor // 50
    valor %= 50

    N20 = valor // 20
    valor %= 20

    N10 = valor // 10
    valor %= 10

    N1 = valor

    print('=-=-=-=-=-=-=-=-=-=')
    print('Serão nescessarias:')
    print(f'{N50} notas de 50')
    print(f'{N20} notas de 20')
    print(f'{N10} notas de 10')
    print(f'{N1} notas de 1')
    print('=-=-=-=-=-=-=-=-=-=')