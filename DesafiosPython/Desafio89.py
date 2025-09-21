#Passo 1-> Definir funções
def linha():
    print('-'*20)

def area(a, b):
    terreno = a * b
    linha()
    print(f'A área do terreno equivale a: {terreno:.1f} metros²')



#Passo 2-> Definir valores de largura e comprimento
print('\nControle de Terrenos')
linha()
num1 = float(input(f'Qual a largura do terreno? [EM METROS] '))
num2 = float(input(f'Qual o comprimento do terreno? [EM METROS] '))

#Passo 3-> Exibir os resultados
area(num1, num2)