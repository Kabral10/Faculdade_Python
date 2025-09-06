#Crie um programa que leia a largura e a altura de uma parede em metros e retorne sua area além da quantidade de tinta para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²

print('--- MEDIDOR DE TINTA E AREA ---\n')

#inserindo dados
a = input('Digite a altura da parede em metros:\n')
l = input('Agora digite a largura em metros:\n')

#calculos
ar = float(a) * float(l)
ti = ar / 2
print(f'A area em m² é {ar}\n')
print(f'Para pintar essa parede sera(ão) necessario(s) {ti} balde(s) de tinta')