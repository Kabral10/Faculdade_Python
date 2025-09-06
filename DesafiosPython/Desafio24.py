#Faça um programa que leia um ano e retorne se ele é ou não bissexto!

#um ano é bissexto se for divisivel por 4! (em casos que terminem 00 por 4 e 400)

#introdução
print('--- Ano bissexto? ---')

#inserção de dado
data = int((input('Qual ano deverá ser verificado?\n')))

#Condicionamento
if( data % 4 == 0 and data % 100 != 0) or (data % 400 == 0):
    print(f'O ano de {data} é bissexto!\n')

else:
    print(f'O ano de {data} não é bissexto!\n')