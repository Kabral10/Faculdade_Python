

nascimento = int(input("Digite o ano de nascimento: "))
ano = 2025
diferença = ano - nascimento

if (diferença < 18):
    print("Você é menor de idade e ainda irá se alistar.")
    print(f"Faltam {18 - diferença} anos para o alistamento.")
elif (diferença > 18):
    print("Você é maior de idade e já deveria ter se alistado.")
    print(f"Você deveria ter se alistado há {diferença - 18} anos.")
else:
    print("Você é exatamente 18 anos e deve se alistar.")