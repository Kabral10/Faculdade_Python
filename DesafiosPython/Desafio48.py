#Faça o computador pensar em um numero de 0 a 5 epara o usuario tentar descobrir qual foi o numero! O programa deverá escrever na tela se o usuario venceu ou perdeu!

#importação de biblioteca para o random
import random

#Introdução
print('--- Jogo Da Adivinhação ---')

#Escolha do computador e do jogador!
EscolhaPC = random.randint(0, 10)
EscolhaUS = int(input('Qual numero você acha que o computador escolheu:\n'))

while EscolhaUS != EscolhaPC:
    print('Você errou. Tente novamente.')
    EscolhaUS = int(input('Qual numero você acha que o computador escolheu:\n'))

#condicionamento simples
print('Parabéns você venceu!!\n' if EscolhaUS == EscolhaPC else 'Você perdeu, é uma pena!\n')