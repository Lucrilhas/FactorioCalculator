import requests
from bs4 import BeautifulSoup
import os
from utils.GetLogger import logger

def download_page(url, output_path):
    """Downloads a single page and saves it to a file."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with open(output_path, "wb") as f:  # Save as binary to handle different encodings
            f.write(response.content)

        logger.debug(f"Downloaded: {url} to {output_path}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading {url}: {e}")
        return False  # Indicate failure
    return True

def get_all_itens(base_path, materials_receipes_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(base_path + materials_receipes_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    itens_divs = soup.find_all("div", {"class": "factorio-icon"})
    itens_links = [i.find("a").get("href") for i in itens_divs]
    for n, i in enumerate(itens_links):
        logger.debug(f"{n+1}/{len(itens_links)}")
        download_page(base_path + i, output_dir[:-1] + i + ".html")
        