#Crie um programa que leia duas notas de um aluno e retorne a sua media

n1 = input('Qual a sua primeira nota? ')
n2 = input('Qual a sua segunda nota? ')

#verificação numerica:
if(n1.isnumeric() and n2.isnumeric() == True):
    
    #Calcula a media de n1 e n2 convertendo ambos para inteiros
    media = (int(n1) + int(n2)) / 2

    #Exibe a media
    print(f'A media das suas notas equivale a: {media}')

else:
    print('Não me surpreende a nota baixa... faça o que foi requisitado!')