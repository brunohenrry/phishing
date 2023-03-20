import os
import requests

def clone_and_upload():
    # Obtendo informações do usuário
    url = input('Digite o URL da página que deseja clonar: ')
    use_ngrok = input('Deseja fazer o upload para o ngrok? (s/n): ')

    # Clonando a página
    response = requests.get(url)
    page_content = response.text
    file_name = url.split('/')[-1]
    with open(file_name, 'w') as f:
        f.write(page_content)

    # Fazendo o upload para o ngrok (se desejado pelo usuário)
    if use_ngrok.lower() == 's':
        os.system(f'ngrok http file://{os.getcwd()}/{file_name}')
    
    # Salvando as informações do usuário em um arquivo
    with open('user_info.txt', 'w') as f:
        f.write(f'URL: {url}\n')
        f.write(f'Usar ngrok: {use_ngrok}\n')

# Exemplo de uso:
clone_and_upload()