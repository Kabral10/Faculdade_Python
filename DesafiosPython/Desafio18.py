#Crie um programa que receba uma frase e mostre: ( Quantas vezes aparece A ), ( Em que posição ela aparece a primeira vez), ( Em que posição aparece a ultima vez)

print('--- DESAFIO LETRA A ---')
f = input('Informe sua frase:\n')
fm = f.lower()

print(f'A letra (a) aparece {fm.count('a')} vezes')
print(f'Sua primeira posição é {fm.find('a')}')
print(f'Sua ultima posição é {fm.rfind('a')}')