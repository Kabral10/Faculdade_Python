tupla = (int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')))

print(f'\nO valor 9 aparece um total de: {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O numero 3 aparece na posição: {(tupla.index(3))}')
else:
    print('Não esxite numero 3 na tupla!')

print(f'Os numeros pares dentro da tupla são:')
for numero in tupla:
    if numero % 2 == 0:
        print(numero)

