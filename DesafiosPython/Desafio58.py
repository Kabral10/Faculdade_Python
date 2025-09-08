print('=-=-=-=-=-=-=-=-=-=-=')
print('| Jogo Par ou Impar |')
print('=-=-=-=-=-=-=-=-=-=-=')
import random

escolha = input('Deseja jogar? [S|N]: ').upper().strip()
print('=-=-=-=-=-=-=-=-=-=-=\n')

#Inicia as vitorias
vitorias = 0

#Loop
while escolha == 'S':
    #JOGADOR
    print('=-=-=-=-=-=-=-=-=-=-=')
    Ejogador = input("Par ou Impar? ").upper().strip()
    Njogador = int(input('Qual numero? [1 a 10] '))
    print('=-=-=-=-=-=-=-=-=-=-=\n')

    #MAQUINA
    Nmaquina = random.randint(1, 10)

    #Soma Para o resultado
    soma = (Njogador + Nmaquina)
    par = soma % 2

    if Ejogador == 'PAR':
        print('=-=-=-=-=-=-=-=-=-=-=')
        print(f"Você escolheu Par! A maquina jogará como Impar!")
        print('=-=-=-=-=-=-=-=-=-=-=\n')
        if soma%2 == 0:
            print('=-=-=-=-=-=-=-=-=-=-=')
            print(f'A maquina escolheu {Nmaquina}')
            print(f'A soma dos numero é: {soma}')
            print('Você ganhou!')
            print('=-=-=-=-=-=-=-=-=-=-=\n')
            escolha = input('Deseja jogar novamente? (S|N): ').upper().strip()
            vitorias += 1
        else:
            print('=-=-=-=-=-=-=-=-=-=-=')
            print(f'A maquina escolheu {Nmaquina}')
            print(f'A soma dos numero é: {soma}')
            print('Você Perdeu!')
            print('=-=-=-=-=-=-=-=-=-=-=')
            print(f'Seu total de vitorias até agora é: {vitorias}')
            print('=-=-=-=-=-=-=-=-=-=-=')
            break

    elif Ejogador == 'IMPAR':
        print('=-=-=-=-=-=-=-=-=-=-=')
        print(f"Você escolheu Impar! A maquina jogará como Par!")
        print('=-=-=-=-=-=-=-=-=-=-=\n')
        if soma%2 == 0:
            print('=-=-=-=-=-=-=-=-=-=-=')
            print(f'A maquina escolheu {Nmaquina}')
            print(f'A soma dos numero é: {soma}')
            print('Você Perdeu!')
            print('=-=-=-=-=-=-=-=-=-=-=')
            print(f'Seu total de vitorias até agora é: {vitorias}')
            print('=-=-=-=-=-=-=-=-=-=-=')
            break
        else:
            print('=-=-=-=-=-=-=-=-=-=-=')
            print(f'A maquina escolheu {Nmaquina}')
            print(f'A soma dos numero é: {soma}')
            print('Você Venceu!')
            print('=-=-=-=-=-=-=-=-=-=-=')
            vitorias += 1
    else:
        print('=-=-=-=-=-=-=-=-=-=-=')
        print('Escolha entre Par e Impar!')
        print('=-=-=-=-=-=-=-=-=-=-=')

print('Saindo do jogo...')
