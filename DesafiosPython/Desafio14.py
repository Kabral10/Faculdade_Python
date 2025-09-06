#Crie um programa q leia o nome completo de uma pessoa e retorne ( O nome com todas letras maiusculas ), ( O nome com todas letras minusculas ), (Quantas letras totais sem considerar espaços)
#( Quantas letras tem o primeiro nome )

print('--- DESAFIO DO NOME ---')

nome = input('Informe o seu nome:\n')
nomed = nome.split()

print(nome.upper())

print(nome.lower())

print(len(nome.strip()))

print(len(nomed[0]))