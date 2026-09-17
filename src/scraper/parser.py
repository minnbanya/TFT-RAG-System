import os
from bs4 import BeautifulSoup
import markdownify

class TFTParser:
    def __init__(self, input_dir: str = "data/raw", output_dir: str = "data/processed"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def html_to_markdown(self, filename: str):
        input_path = os.path.join(self.input_dir, filename)
        output_filename = filename.replace('.html', '.md')
        output_path = os.path.join(self.output_dir, output_filename)

        with open(input_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        content_body = soup.find('div', id='patch-notes-container')
        if not content_body:
            content_body = soup.find('article')

        if content_body:
            md_text = markdownify.markdownify(str(content_body), heading_style="ATX")

            clean_md = "\n".join([line for line in md_text.splitlines() if line.strip()])

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(clean_md)

            print(f"Parsed and saved Markdown to {output_path}")
            return output_path

        else:
            print(f"Warning: Could not find main content body in {filename}")
            return None
if __name__ == "__main__":
    parser = TFTParser()
    parser.html_to_markdown("latest_patch.html")