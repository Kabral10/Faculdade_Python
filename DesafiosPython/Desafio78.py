listanumerica = [[], []]


for i in range(7):
    numero = int(input(f'Qual valor será adicionado na {i}ª posição? '))
    if numero % 2 == 0:
        listanumerica[0].append(numero)
    else:
        listanumerica[1].append(numero)

listanumerica[0].sort()
listanumerica[1].sort()

print('=-'*19)
print(f'Os valores pares foram: {listanumerica[0]}')
print(f'Os valores impares foram: {listanumerica[1]}')