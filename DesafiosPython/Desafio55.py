escolha = 'S'
total = 0
quantidade = 0
maior_numero = None
menor_numero = None

while escolha == 'S':
    numero = int(input('Digite um numero: '))
    total += numero
    quantidade += 1

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

    escolha = input('Deseja continuar?\n(S/N): ').strip().upper()

media = total / quantidade if quantidade > 0 else 0


print(f'A media dos numeros é: {media:.2f}')
print(f'O maior dos numero é: {maior_numero}')
print(f'O menor dos numero é: {menor_numero}')

print('finalizado com sucesso!')
print('Obrigado por utilizar o sistema!')