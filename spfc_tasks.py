import os
import requests
import csv
from datetime import date

# Crie uma pasta 'logs' se não existir
if not os.path.exists('logs'):
    os.makedirs('logs')

# URLs dos sites
sites = {
    'ge': 'https://ge.globo.com/futebol/',
    'cnn': 'https://www.cnnbrasil.com.br/esportes/',
    'gazeta': 'https://www.gazetaesportiva.com/',
    'espn': 'https://www.espn.com.br/futebol/',
}

# Função para buscar notícias e salvar em CSV
def buscar_e_salvar_noticias(site):
    url = sites[site]
    response = requests.get(url)
    # Aqui você deve analisar o conteúdo da página e extrair as informações relevantes
    # Exemplo: títulos, resumos, links das notícias
    # Verifique se a palavra-chave "venda" ou "compra" está presente nas notícias
    # Salve os dados em um arquivo CSV com o nome apropriado
    today = date.today().strftime("%Y-%m-%d")
    filename = f"resumo_noticias_do_dia_{today}_{site}.csv"
    with open(f'logs/{filename}', 'w', newline='') as csvfile:
        fieldnames = ['titulo', 'resumo', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # Escreva os dados no arquivo CSV (exemplo fictício)
        writer.writerow({'titulo': 'Notícia 1', 'resumo': 'Resumo da notícia 1', 'link': 'https://example.com/noticia1'})
        writer.writerow({'titulo': 'Notícia 2', 'resumo': 'Resumo da notícia 2', 'link': 'https://example.com/noticia2'})

# Execute a função para cada site
buscar_e_salvar_noticias('ge')
buscar_e_salvar_noticias('cnn')
buscar_e_salvar_noticias('gazeta')
buscar_e_salvar_noticias('espn')

print("Notícias salvas em arquivos CSV na pasta 'logs'.")
