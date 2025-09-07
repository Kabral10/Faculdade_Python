print('Escolha uma opção:\n1: somar\n2: multiplicar\n3: maior\n4: novos numeros\n5: sair do programa')

escolha = int(input('Escolha:'))
n1 = int(input('Escolha um numero:\n'))
n2 = int(input('Escolha outro numero:\n'))

while escolha:
    if escolha == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        escolha = int(input('E agora, o que deseja fazer?\nescolha:'))
    elif escolha == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
        escolha = int(input('E agora, o que deseja fazer?\nescolha:'))
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}!')
        else:
            print(f'{n1} não é maior que {n2}!')
        escolha = int(input('E agora, o que deseja fazer?\nescolha:'))
    elif escolha == 4:
        print('Mundando os numeros!')
        n1 = int(input('Escolha um numero:\n'))
        n2 = int(input('Escolha outro numero:\n'))
        escolha = int(input('E agora, o que deseja fazer?\nescolha:'))
    elif escolha == 5:
        print('Saindo do programa...')
        break
