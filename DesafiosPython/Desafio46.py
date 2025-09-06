soma_idade = 0
homem_mais_velho = 0
mulheres_menores = 0
nome_homem_mais_velho = ''

for i in range(1, 5):
    nome = input(f'\nInforme o nome da {i}ª pessoa: ').capitalize()
    sexo = input(f'Informe o sexo da {i}ª pessoa (M/F): ').strip().upper()
    idade = int(input(f'Informe a idade da {i}ª pessoa: '))
    
    soma_idade += idade
    
    if sexo == 'M' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menores += 1

media_idade = soma_idade / 4
print(f'\nA média de idade do grupo é de {round(media_idade)} anos.')

if homem_mais_velho > 0:
    print(f'O homem mais velho se chama {nome_homem_mais_velho}.')
else:
    print('Não há homens nesse grupo.')

print(f'Ao todo são {mulheres_menores} mulheres com menos de 20 anos.')