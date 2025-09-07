sexo = input('insira seu sexo (M/F): ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('insira seu sexo (M/F): ').upper()

print(f'Seu sexo é {sexo}')