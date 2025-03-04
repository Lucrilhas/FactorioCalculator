from bs4 import BeautifulSoup
import os
from utils.GetLogger import logger

def convert_recipe_to_dict(htmls):
    resposta = {
        'ingredientes': list(),
        'resultados': list(),
        'tempo': None,
    }
    
    texto = htmls.get_text(separator=' ', strip=True)
    partes = texto.split('→')
    antes = partes[0].strip().split(" + ")
    depois = partes[1].strip().split(" + ") if len(partes) > 1 else ""

    resposta['tempo'] = antes.pop(0)

    childrens = htmls.findChildren()
    names = [childrens[i].find('a').get('href') for i in range(1, len(childrens), 5)]
    names.pop(0)

    for i, a in enumerate(antes):
        resposta['ingredientes'].append([a, names[i]])
    for i, d in enumerate(depois):
        resposta['resultados'].append([d, names[i + len(antes)]])

    return resposta
    
def process_item(item, file_path):
    print(file_path + item + ".html")
    with open(file_path + item + ".html", "r", encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p', string="Recipe\n")
    paragraphs_parents_td = [p.parent for p in paragraphs]
    td_parents_tr = [t.parent for t in paragraphs_parents_td]
    next_td = [t.find_next_sibling('tr') for t in td_parents_tr]
    crafts = [convert_recipe_to_dict(x) for x in next_td]

    print(crafts)
