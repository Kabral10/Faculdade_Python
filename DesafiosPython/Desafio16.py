#Crie um programa que recebe o nome de uma cidade e retorna a informação ( se o nome começa com "santo" ou não )

print('--- DESAFIO CIDADE ---')
n = input('Informe o nome da cidade:\n')
nm = n.lower().split()

if('santo' in nm[0]):
    print('O nome da cidade começa com Santo!')
else:
    print('Não há Santo no nome dessa cidade!')