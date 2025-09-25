#passo 1 - biblioteca e funções
import requests

def verificar_acesso(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'\033[0;32mO site {url} está acessivel!')
            return True
        else:
            print(f'\033[0;31mO site {url} não está acessivel!')
            return False
    except requests.exceptions.RequestException as e:
        print(f'\033[0;31mErro ao acessar o site {url}: {e}')
        return False

verificar_acesso('http://pudim.com.br/')
verificar_acesso('http://www.python.og')