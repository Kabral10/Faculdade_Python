#Crie um algoritmo q le o salario de um funcionario e retorna seu valor com 15% de aumento

print('--- SALARIO NOVO ---')

s = input('Qual o valor do seu salario com os centavos:\n')
a = float(s) * (15/100)
sca = float(s) + a

print(f'o seu novo salario com 15% de aumento é: {sca} !!')