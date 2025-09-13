matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

print('\n'+('=-'*19))

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('=-'*19)

print(f'A soma de todos valores pares é: {pares}')
print(f'A soma de todos valores da terceita coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O mair valor da segunda linha é: {max(matriz[1])}.')

print('=-'*19)
