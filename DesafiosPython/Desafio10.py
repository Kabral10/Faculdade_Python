#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e retorne  quantos dolares ela pode comprar
#considere o dolar 3,27 reais

#Apresentação
print('---PROGRAMA DE CAMBIO---')

#inserção de dados
r = input('Quantos reais você tem? ')

#conversão do real para dolar
d = float(r)/3.27

#verificação de numero:
if(r.isnumeric() == True):
    print(f'Você pode comprar U${d:.3}')

else:
    print('Quer converter real ou burrice ?\n')
