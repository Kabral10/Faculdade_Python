# Crie um programa que receba um valor em metros e retorne seu valor em centimetros e milimetros

#Entrada de dado na variavel n
n = input('Quantos metros gostaria de converter para cm e mm? ')

#Verificação de numero
if(n.isnumeric() == True):
    
    #Variaveis Calculadas
    nc = int(n) * 100
    nm = int(n) * 1000

#Exibição da informação
    print(f'O valor selecionado ( {n} metros ) em centimetros é ( {nc} cm ), e em milimetros é ( {nm} mm ).')

else:
    print('Você não forneceu uma informação adequada!!')