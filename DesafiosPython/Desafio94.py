#Passo 1 -> Criar a função e importar datetime
import datetime

def voto(nascimento):
    ano_atual = datetime.date.today().year
    idade = (ano_atual - nascimento)
    if idade <= 15:
        print(f'Com {idade} anos: NÃO VOTA ')
    elif (15 < idade < 18) or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATORIO')
def linha():
    print('-=' * 30)

#Passo 2 -> Definir os parametros
linha()
voto(int(input('Digite o ano de nascimento: ')))
linha()