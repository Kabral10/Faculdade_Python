#Crie um programa que leia 5 valores numerico e guarde em uma lista!
#No final mostre quais foram ( o maio e o menor numero ) e suas posições na lista

listadevalores = list()
for i in range(5):
    listadevalores.append(int(input(f'Digite um numero para a posição {i} lista: ')))

print(f'a lista criada contem:\n{listadevalores}')
print(f'O maior numero da lista é {max(listadevalores)} e está na posição {listadevalores.index(max(listadevalores))}')
print(f'O menor numero da lista é {min(listadevalores)} e está na posição {listadevalores.index(min(listadevalores))}')
