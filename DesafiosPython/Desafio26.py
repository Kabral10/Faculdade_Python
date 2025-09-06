#Crie um programa q receba um salario de funcionario e de uma promoção ao mesmo! 10% para salarios maiores que 1250,00 e 15% para menores ou iguais a 1250,00

#introdução
print('--- Promoção Salarial ---')

#informações
salario = float(input('Qual o seu salario?\n'))

#calculos
promo_dez = salario + (salario * (10/100))
promo_quinze = salario + (salario * (15/100))

#Condições
if salario > 1250.00:
    print(f'\nO seu salario após a promoção de 10% é de R${promo_dez} !\n')
else:
    print(f'\nO seu salario após a promoção de 15% é de R${promo_quinze} ! \n')