# Crie um programa q leia o nome de uma pessoa e retorne se o nome da pessoa contem "SILVA"

print('--- DESAFIO NOME ---')
n = input('Informe um nome:\n')
nm = n.lower()

if('silva' in nm):
    print('Existe Silva nesse nome!')
else:
    print('Este nome não contém Silva')