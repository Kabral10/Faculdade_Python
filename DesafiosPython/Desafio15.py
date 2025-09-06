# faça um programa que leia um numero entra 1 e 9999 e retorne as informações do numero separadamente ( unidade, dezena... )

print('--- DESAFIO DOS NUMEROS ---')
n = input('Informe o número:\n')

if(len(n) == 1):
    print(f'O numero escolhido é {n}')
    print(f'Unidade:{n[0]}')
elif(len(n) == 2):
    print(f'O numero escolhido é {n}')
    print(f'Unidade:{n[1]}')
    print(f'Dezena: {n[0]}')
elif(len(n) == 3):
    print(f'O numero escolhido é {n}')
    print(f'Unidade:{n[2]}')
    print(f'Dezena: {n[1]}')    
    print(f'Centena: {n[0]}')
else:
    print(f'O numero escolhido é {n}')
    print(f'Unidade:{n[3]}')
    print(f'Dezena: {n[2]}')    
    print(f'Centena: {n[1]}')
    print(f'Milhar: {n[0]}')
