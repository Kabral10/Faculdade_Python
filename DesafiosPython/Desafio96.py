#Passo 1 -> importação e definição

def ficha():
    nome = str(input('Nome do jogador: '))
    gols = str(input('Quantidade de gols: '))
    if gols == '':
        gols = 0
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
def linha():
    print('-=' * 30)

linha()
ficha()
linha()
