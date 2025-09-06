#Crie um programa que leia duas notas de um aluno, calcule a média e mostre a situação do aluno.

nota1 = float(input('Digite a primeira nota: ')) 
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"Sua média foi {media:.1f}. Você está REPROVADO.")
elif media >= 5.0 and media < 7.0:
    print(f"Sua média foi {media:.1f}. Você está em RECUPERAÇÃO.")
else:
    print(f"Sua média foi {media:.1f}. Você está APROVADO.")