ZeroVinte = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input("escolha um numero: [0 a 20] "))
    if 0 <= numero <= 20:
        print(f'O numero {numero} por extenso é {ZeroVinte[numero]}')
    elif numero < 0:
        print('Finalizando programa...')
        break
    else:
        print('numero não é valido')