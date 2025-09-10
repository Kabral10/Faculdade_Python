#Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas as letras minúsculas
# -> Quantas letras o nome tem ( sem espaço )
# -> Quantas letras tem o primeiro nome

nome = input('Qualo seu nome: ')
nomeSeparado = nome.split()

print(f'O seu nome todo em maiúsculo: {nome.upper()} ')
print(f'O seu nome todo em minúsculo: {nome.lower()} ')
print(f'O seu nome tem {len(''.join(nomeSeparado))} letras sem contar os espaços')
print(f'O seu primeiro nome tem {len(nomeSeparado[0])} letras')