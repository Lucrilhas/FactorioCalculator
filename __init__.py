from functions.CrawlWiki import crawl_wiki


if __name__ == "__main__":
    BASE_URL = "https://wiki.factorio.com/"
    OUTPUT_DIR = "data/pages/factorio_wiki"
    crawl_wiki(BASE_URL, OUTPUT_DIR)