#Crie um programa que receba o valor de três retas e diga se elas podem formar um triangulo

#introdução
print('\n--- Triangulo ou não? ---\n')

#Informações
l1 = int(input('Qual o valor do primeiro lado:\n'))
l2 = int(input('Qual o valor do segundo lado:\n'))
l3 = int(input('Qual o valor do terceiro lado:\n'))

#Condicionamento || A soma de quaiquer lados deve ser maior que o terceiro
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Sim, é possivel fazer um triangulo com esses valores!\n')
else:
    print('Não é possivel fazer um triangulo com tais valores!\n')