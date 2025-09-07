numero = int(input('Qual numero irá iniciar a sequencia de fibonacci?'))
numero2 = int(input('Qual será o segundo numero?'))
limite = 20
contador = 0

print(numero)
print(numero2)

while contador < limite-2:
    proximo = numero + numero2
    print(proximo)
    numero = numero2
    numero2 = proximo
    contador += 1