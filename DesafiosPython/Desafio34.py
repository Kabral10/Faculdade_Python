#adicione ao programa do triangulo um meio de mostrar que tipo de triagulo será formado, mantendo sua função antiga 

#introdução
print('\n--- Triangulo ou não? ---\n')

#Informações
l1 = int(input('Qual o valor do primeiro lado:\n'))
l2 = int(input('Qual o valor do segundo lado:\n'))
l3 = int(input('Qual o valor do terceiro lado:\n'))

#Condicionamento || A soma de quaiquer lados deve ser maior que o terceiro
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('\nSim, é possivel fazer um triangulo com esses valores!')
    if l1 == l2 == l3:
        print('E ele é um triangulo equilatero!\n')
    elif l1 != l2 != l3 != l1:
        print('E ele é um triangulo escaleno!\n')
    else:
        print('E ele é um triangulo isosceles!\n')
else:
    print('\nNão é possivel fazer um triangulo com tais valores!\n')