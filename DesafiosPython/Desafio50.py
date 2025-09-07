print('--- Fatorando ---')

numero = int(input('Escolha um numero:'))
fatorial = 1

#fatorando
for i in range(numero, 0, -1):
    fatorial *= i
    print(f'{numero}X{i}')

print(f'O fatorial de {numero} é {fatorial}')