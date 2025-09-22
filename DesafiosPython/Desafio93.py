#Passo 1-> definir funções e importar biblioteca
import random, time
lista = list()

def linha():
    print('-'*30)
def sorteia():
    print(f'Sorteando 5 valores para a lista:', end=' ')
    for n in range(0,5):
        numero = (random.randint(1,10))
        time.sleep(0.4)
        print(f'{numero}', end=' ')
        lista.append(numero)
    print('Pronto!')
def somapar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares é: {soma}')
def limpa():
    lista.clear()

#Passo 2 -> Exibir Resultados
linha()
sorteia()
somapar()
linha()
limpa()
sorteia()
somapar()
linha()
limpa()
sorteia()
somapar()
linha()