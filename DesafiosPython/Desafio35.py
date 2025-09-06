#Jokempo

import random


print('\n-- Jokenpo --\n')

escolha = int(input('Faça sua escolha:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n'))
escolha_pc = random.randint(1, 3)

if escolha == 1:
    if escolha_pc == 1:
        print('Empate! Ambos escolheram Pedra.')
    elif escolha_pc == 2:
        print('Você perdeu! Papel cobre Pedra.')
    else:
        print('Você ganhou! Pedra corta Tesoura.')
elif escolha == 2:
    if escolha_pc == 1:
        print('Você ganhou! Papel cobre Pedra.')
    elif escolha_pc == 2:
        print('Empate! Ambos escolheram Papel.')
    else:
        print('Você perdeu! Tesoura corta Papel.')
else:
    if escolha_pc == 1:
        print('Você perdeu! Pedra cobre Tesoura.')
    elif escolha_pc == 2:
        print('Você ganhou! Tesoura corta Papel.')
    else:
        print('Empate! Ambos escolheram Tesoura.')