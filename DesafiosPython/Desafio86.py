Dados = dict()
gols = []

Dados['Jogador'] = str(input('Nome do jogador: ')).title().strip()
Dados['Partidas'] = int(input(f'Quantas partidas {Dados['Jogador']} jogou? '))

for i in range(1 ,Dados['Partidas']+1):
    gol = int(input(f'Quantos gols na partida {i}? '))
    gols.append(gol)

Dados['Gols'] = gols
Dados['Total de Gols'] = sum(gols)

#IMPRIMINDO RESULTADOS
print('=-'*15+'=')
print(Dados)

print('=-'*15+'=')
print(f'O jogador se chama: {Dados["Jogador"]}')
print(f'{Dados['Jogador']} fez respectivamente {Dados['Gols']} gols em suas partidas')
print(f'{Dados['Jogador']} tem um total de {Dados["Total de Gols"]} gols!')

print('=-'*15+'=')
print(f'O jogador {Dados['Jogador']} jogou {Dados["Partidas"]} partidas.')

for i, g in enumerate(gols):
    print(f'    => na pardida {i+1}: fez {g} gol(s)')

print(f'Foi um total de {Dados["Total de Gols"]} gols.')