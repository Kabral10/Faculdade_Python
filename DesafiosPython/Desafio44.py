maior = 0
menor = 0
for i in range (1, 7+1):
    nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = 2025 - nascimento

    if idade >= 18:
        print(f'Essa pessoa tem {idade} anos, portanto é maior de idade.')
        maior += 1
    else:
        print(f'Essa pessoa tem {idade} anos, portanto é menor de idade.')
        menor += 1
        
print(f'\n {maior} pessoas são maiores de idade e {menor} pessoas são menores de idade.')