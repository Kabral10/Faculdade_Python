#Crie um programa que leia um numero inteiro e retorne se ele é par ou impar!

#Apresentação
print('\n--- Par ou Impar ---')

#Informações
numero = int(input('Qual numero deseja verificar:\n'))

#Condições
if numero % 2 == 0:
    print(f'O numero {numero} é par!\n')
else:
    print(f'O numero {numero} é impar\n')