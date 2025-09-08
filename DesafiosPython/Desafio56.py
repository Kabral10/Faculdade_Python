s = 0
quantidade = 0

while True:
    n = int(input('digite um numero: (999 para sair) '))
    if n == 999:
        break
    s += n
    quantidade += 1
print(f'A soma dos {quantidade} numeros é: {s}')
print('finalizado com sucesso!')