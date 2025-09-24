#Passo 1 -> importar e definir
import time
def titulo(msg, estilo=1, texto=37, fundo=42):
    tam = len(msg) + 4
    print(f"\033[{estilo};{texto};{fundo}m", end="")
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print("\033[m", end='')

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", estilo=1, texto=30, fundo=46)
    print("\033[7m", end='')
    help(com)
    print("\033[m", end='')

def sistema():
    while True:
        titulo("Sistema de Ajuda PythonHelp", estilo=1, texto=30, fundo=42)
        comando = input("Função da Biblioteca -> ")
        if comando.upper() == "FIM":
            titulo("Finalizando...", estilo=1, texto=30, fundo=41)
            break
        else:
            time.sleep(1.2)
            ajuda(comando)
            time.sleep(1.2)

    titulo("Até, Logo!", 1,30,47)


sistema()