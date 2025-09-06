#Crie um programa que receba o nome completo de uma pessoa e retorne em seguida o primeiro e o ultimo nome separadamente

print('--- DESAFIO NOME CHATO ---')
n = input('Informe um nome:\n')
nm = n.lower().split()

if(len(nm) == 1):
    print(f'\nO primeiro nome é {nm[0]}')

else:
    print(f'\nO primeiro nome é {nm[0]}\nO último nome é {nm[-1]}')