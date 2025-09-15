jogadores = list()
dados = dict()
gols = []
escolha = 'S'

#Loop De dados do jogador
while escolha == 'S':
    print('-'*10)
    dados['Jogador'] = str(input('Nome do jogador: ')).title().strip()
    dados['partidas'] = int(input(f'Quantas partidades {dados["Jogador"]} jogou? '))

    for p in range(1, dados['partidas']+1):
        gol = int(input(f'Quantos gols na partida {p}? '))
        gols.append(gol)

    dados['Gols'] = gols.copy()
    dados['Total de gols'] = sum(gols)

    jogadores.append(dados.copy())

    dados.clear()
    gols.clear()

    print('-'*10)
    escolha = str(input('\nDeseja continuar? [S/N] ')).strip().upper()

#Exibição de informações
print('=-'*15+'=')
print(f"{'Cod':<8}{'nome':<12}{'gols':<18}{'total':>8}")

for i, p in enumerate(jogadores):
    print(f"{i:<8}{p['Jogador']:<12}{str(p['Gols']):<18}{p['Total de gols']:>8}")


#Desempenho individual
print('=-'*15+'=')
while True:
    opc = int(input('Deseja mostrar os dados de qual jogador? '))

    if 0 <= opc <= len(jogadores):
        print(f'-- Levantamento do jogador {jogadores[opc]['Jogador']}')
        for j, g in enumerate(jogadores[opc]['Gols']):
            print(f'\tNa partida {j+1}: {g} gols')

    if opc == 999:
        print('=-'*15)
        print('Finalizando...')
        break