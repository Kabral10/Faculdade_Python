#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado, a multa custa 7 reais por cada km acima do limite

#Introdução
print('--- De olho na estrada ---')

#Definição de variaveis
velocidade = float(input('Qual a velocidade do carro:\n'))
limite = 80.0
multa = 7 #Por kilometro

#funções
diferenca = velocidade - limite
Calc_Multa = diferenca * 7

#exibição
if velocidade > limite:
    print(f'Você está {diferenca}Km acima do limite e vai receber uma multa de R${Calc_Multa:.2f} ')
else:
    print('Você está em uma velocidade permitida!')