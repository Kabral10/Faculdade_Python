import random
import time

lista = list()
ranking = dict()

#sorteio de valores
for c in range(1,5):
    ranking['Jogador'] = c
    ranking['resultado'] = random.randint(1, 6)
    lista.append(ranking.copy())

print('=-'*15 + '='), time.sleep(1)
print('Valores sorteados:'), time.sleep(1)
for j in range(len(lista)):
    print(f'   O jogador{lista[j]["Jogador"]} tirou: {lista[j]["resultado"]}')
    time.sleep(1)

#ordenando a lista pelo resultado ( maior -> menor )
ranking_final = sorted(lista, key=lambda x: x['resultado'], reverse=True)

print('=-'*15 + '='), time.sleep(1)
print('Ranking dos jogadores:'), time.sleep(1)
for i, jogador in enumerate(ranking_final, start=1):
    print(f'   {i}º lugar: jogador{jogador["Jogador"]} com {jogador["resultado"]}')
    time.sleep(1)
