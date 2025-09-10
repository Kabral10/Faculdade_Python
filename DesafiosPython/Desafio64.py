nome = input('Qual o seu nome?\n').title()

NomeSeparado = nome.split()

print(f'Seu primeiro nome é {NomeSeparado[0]}')
print(f'Seu ultimo nome é {NomeSeparado[-1]}')