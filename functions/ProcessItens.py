from bs4 import BeautifulSoup
import os
from utils.GetLogger import logger
from utils.DataClasses import ItemQuant, Recipe


def convert_recipe_to_dict(htmls):
    resposta = Recipe()

    texto = htmls.get_text(separator=' ', strip=True)
    partes = texto.split('→')
    ings = partes[0].strip().split(" + ")
    res = partes[1].strip().split(" + ") if len(partes) > 1 else []

    resposta.tempo = int(ings.pop(0))

    childrens = htmls.find_all()  # Use find_all instead of findChildren (more standard)
    names = [child.find('a')['href'] for i, child in enumerate(childrens) if i % 5 == 1 and child.find('a')]
    names.pop(0) #remove o primeiro item da lista, o tempo.

    for i, a in enumerate(ings):
        resposta.input.append(ItemQuant(item=names[i], quant=a))

    for i, d in enumerate(res):
        resposta.output.append(ItemQuant(item=names[i + len(ings)], quant=d))

    return resposta


def process_item(item, file_path):
    """
    Processes a recipe item by reading its HTML file, extracting recipe details, and printing the extracted data.

    Args:
        item: The name of the recipe item.
        file_path: The path to the directory containing the HTML files.
    """

    file_name = os.path.join(file_path, f"{item}.html") # Use os.path.join for better path handling

    try:
        with open(file_name, "r", encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_name}")
        return  # Exit if the file doesn't exist
    except Exception as e:
        print(f"Error reading file {file_name}: {e}")
        return

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <p> tags with the specific string "Recipe\n"
    paragraphs = soup.find_all('p', string="Recipe\n")

    # Extract the <tr> elements containing the recipe information.  Chain operations in one line for conciseness.
    crafts = [convert_recipe_to_dict(p.parent.parent.find_next_sibling('tr')) for p in paragraphs]

    for c in crafts:
        print(c)