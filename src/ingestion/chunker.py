import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

class TFTChunker:
    def __init__(self, input_dir: str = "data/processed"):
        self.input_dir = input_dir

        # Setting chunk size to 700, with overlap of 100 to prevent cutoffs
        self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            encoding_name = "cl100k_base",
            chunk_size=700, 
            chunk_overlap=100,
            # Markdown headers/paragraphs
            separators=["\n\n", "\n", r"(?<=\. )", " ", ""]
        )

    def chunk_file(self, filename: str):
        filepath = os.path.join(self.input_dir, filename)

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Could not find {filepath}")

        with open(filepath, 'r', encoding="utf-8") as f:
            text = f.read()

        chunks = self.text_splitter.split_text(text)
        print(f"Successfully split {filename} into {len(chunks)} chunks")

        return [{"text": chunk, "source": filename} for chunk in chunks]

if __name__ == "__main__":
    chunker = TFTChunker()
    chunks = chunker.chunk_file("latest_patch.md")

    if chunks:
        print("\n--- Sample Chunk (first 300 characters) ---")
        print(chunks[0]['text'][:300])
        print("-------------------------------------------")
