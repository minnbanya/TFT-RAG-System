import os
import requests
from bs4 import BeautifulSoup

class TFTPatchSpider:
    def __init__(self, output_dir: str="data/raw"):
        self.base_url = "https://teamfighttactics.leagueoflegends.com/en-us/news/tags/patch-notes/"
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_patch_list(self):
        print(f"Fetching patch list from {self.base_url}")
        response = requests.get(self.base_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        article_links = []
        for a_tag in soup.find_all('a', href=True):
            if '/news/game-updates/teamfight-tactics-patch-' in a_tag['href']:
                full_url = f"https://teamfighttactics.leagueoflegends.com{a_tag['href']}"
                if full_url not in article_links:
                    article_links.append(full_url)

        return article_links

    def download_html(self, url:str, filename:str):
        print(f"Downloading {url}")
        response = requests.get(url)
        response.raise_for_status()

        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Saved raw HTML to {filepath}")
        return filepath

if __name__ == "__main__":
    spider = TFTPatchSpider()
    urls = spider.fetch_patch_list()
    if urls:
        spider.download_html(urls[0], "latest_patch_html")
