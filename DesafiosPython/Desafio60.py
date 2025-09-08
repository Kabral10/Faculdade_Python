
TotalGasto = 0
continuar = 'S'
caro = 0
Pmaisbarato = 0
NomeProdutoBarato = ''


while True:
    if continuar == 'S':
        Pnome = input('Nome do Produto: ').capitalize().strip()
        Pvalor = float(input('Valor do Produto: R$'))

        TotalGasto += Pvalor

        if Pvalor > 1000:
            caro += 1

        if Pmaisbarato == 0 or Pvalor < Pmaisbarato:
            Pmaisbarato = Pvalor
            NomeProdutoBarato = Pnome

        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
        while continuar not in ['S', 'N']:
            continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()


    elif continuar == 'N':
        print('----- FIM DO PROGRAMA -----')
        print(f'O total da compra foi R${TotalGasto}')
        if caro > 1:
            print(f'Temos {caro} produtos custando mais de 1000 reais!')
        elif caro == 1:
            print(f'Temos {caro} produto custando mais de 1000!')
        else:
            print(f'Nenhum produto custa mais de 1000!')
        print(f'O produto mais barato é {NomeProdutoBarato} e custa R${Pmaisbarato:.2f}')
        break