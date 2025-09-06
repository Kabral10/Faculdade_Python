#Crie um programa que receba dois numeros e retorne qual é o maior

Numero1 = int(input('Digite um número inteiro: '))
Numero2 = int(input('Digite outro número inteiro: '))

if Numero1 > Numero2:
    print(f"O valor {Numero1} é maior que o valor {Numero2}.")
elif Numero1 < Numero2:
    print(f"O valor {Numero2} é maior que o valor {Numero1}.")
else:
    print("Os dois números são iguais.")