#A confederação nacional de natação precisa de um programa que leia o ano de nasciento de um atleta e mostre sua categoria de acordo com sua idade (até 9 anos mirim , até 14 infantil , até 19 junior , até 20 senior , maior master)

ano = int(input("Digite o ano de nascimento do atleta: "))
idade = 2025 - ano

if idade <= 9:
    print(f"O atleta tem {idade} anos e sua categoria é MIRIM.")
elif idade <= 14:
    print(f"O atleta tem {idade} anos e sua categoria é INFANTIL.")
elif idade <= 19:
    print(f"O atleta tem {idade} anos e sua categoria é JUNIOR.")
elif idade <= 20:
    print(f"O atleta tem {idade} anos e sua categoria é SENIOR.")
else:
    print(f"O atleta tem {idade} anos e sua categoria é MASTER.")