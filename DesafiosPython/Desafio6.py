#Crie um programa que receba um numero e retorne seu dobro , triplo e raiz quadrada

n = input('Digite seu numero: ')

#Caso seja um numero o codigo é executado, caso contrario executa o else
if(n.isnumeric() == True):
    n2 = int(n) * 2
    n3 = int(n) * 3
    rn = float(n) **(1/2)

    print(f'O numero escolhido foi {n}')
    print(f'Seu dobro é {n2}')
    print(f'Seu triplo é {n3}')
    print(f'Sua raiz quadrada é {rn:.3}')
else:
    print('Você é um abestado.. Faça oque lhe foi pedido!!')