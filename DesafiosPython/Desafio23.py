#Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando 0,50 reais por Km para viagens de até 200Km e 0,45 para viagens mais longas

#Introdução
print('\n--- Calculo de Passagens ---')

#Adicionando Informação
distancia = float(input('Qual a distancia da viagem?\n'))

#Funções
Calc_normal = distancia * 0.50 #valor até 200Km
Calc_longo = distancia * 0.45 #valor de viagens acima de 200Km

#Condicionamento
if distancia <= 200.00:
    print(f'\nA sua viagem irá custar R${Calc_normal:.2f} pois sua distancia é de {distancia:.2f}Km')
else:
    print(f'\nSua viagem irá custar R${Calc_longo:.2f} pois sua distancia é de {distancia:.2f}Km')

print('Boa viagem!\n')