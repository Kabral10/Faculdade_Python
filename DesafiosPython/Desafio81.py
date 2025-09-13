import random
lista = list()
jogos = int(input('Quantos jogos deseja gerar? '))

print('\n' + '='+('-='*19))

print(f'Sorteando {jogos} jogos')

for c in range(jogos):
        for i in range(6):
            gerador = random.randint(1, 60)
            lista.append(gerador)
        print(lista)
        lista.clear()

print('='+'-='*19)
