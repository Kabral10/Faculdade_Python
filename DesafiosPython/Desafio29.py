#Escreva um programa q leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal

numero = int(input("Digite um número inteiro: "))
opcao = int(input("Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nDigite a opção desejada: "))

if opcao == 1:
    print(f"O número {numero} em binário é {bin(numero)[2:]}")
elif opcao == 2:
    print(f"O número {numero} em octal é {oct(numero)[2:]}")
elif opcao == 3:
    print(f"O número {numero} em hexadecimal é {hex(numero)[2:]}")