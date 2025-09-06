#Crie um programa que le o preço de um produto e retorna seu valor com 5% de desconto
print('--- DESCONTÃO ---\n')

v = input('Qual o valor do produto?\n')

d = float(v) * (5/100) # valor descontado

vcd = float(v) - d
print(f'O valor do produto após os 5% de desconto é de {vcd:.4} reais!')