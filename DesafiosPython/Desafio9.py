#Crie um programa que receba um numero ( inteiro qualquer ) e retorne sua tabuada

#Boas vindas // Definição da tabuada
print('---TABUADA---\n')
n = input('Deseja ver a tabuada de qual numero? ')

#Verificação numerica
if(n.isnumeric() == True):
    print(f'--- TABUADA DE {n} ---\n')

    #Tabuada em uma linha.. Cada \n é um paragrafo da tabuada!
    print(f'{n}x1 = {int(n)*1} \n{n}x2 = {int(n)*2} \n{n}x3 = {int(n)*3} \n{n}x4 = {int(n)*4} \n{n}x5 = {int(n)*5} \n{n}x6 = {int(n)*6} \n{n}x7 = {int(n)*7} \n{n}x8 = {int(n)*8} \n{n}x9 = {int(n)*9} \n{n}x10 = {int(n)*10}\n')

else:
    print(f'Creio que não existe uma tabuada de ({n}) estude mais!!')