peso = float(input('Digite seu peso (kg): '))
menor_peso = peso
maior_peso = peso

for i in range(1, 5):
    peso = float(input('Digite seu peso (kg): '))
    if peso < menor_peso:
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso

print(f'O maior peso lido foi {maior_peso}kg \ne o menor peso lido foi {menor_peso}kg')