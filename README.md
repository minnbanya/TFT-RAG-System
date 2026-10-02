# TFT RAG System

A production-grade, domain-specific Retrieval-Augmented Generation (RAG) system built to answer questions about Teamfight Tactics (TFT) patch notes. 

Unlike standard RAG demos, this project focuses on **trustworthiness, engineering maturity, and automated evaluation**. It features hybrid retrieval, local cross-encoder re-ranking, strict citation enforcement, and an automated LLM-as-a-judge evaluation pipeline.

## Tech Stack

This project was built using a hybrid approach of local open-source models for retrieval and a free-tier cloud API for generation and evaluation:

* **Orchestration:** LangChain
* **Vector Database:** Weaviate (Local Docker Deployment)
* **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2` running locally)
* **Re-ranking:** Cross-Encoder (`ms-marco-MiniLM-L-6-v2` running locally)
* **Generation & Judging LLM:** Google Gemini (`gemini-3.5-flash` via the modern `google-genai` SDK)
* **Evaluation Framework:** Ragas
* **Data Ingestion:** BeautifulSoup4, Markdownify

## Architecture & Phases

The system was developed in three distinct phases to ensure production readiness:

### Phase 1: The Baseline Pipeline
* **Data Ingestion & Parsing:** Scrapes official TFT HTML patch notes and converts them into clean Markdown.
* **Token-Aware Chunking:** Splits text into strict 500-800 token chunks with a 100-token overlap to preserve context boundaries.
* **Grounded Citations:** The generation prompt explicitly maps LLM claims back to specific chunk and source document identifiers (e.g., `[Source: latest_patch.md - Chunk 1]`).

### Phase 2: Production Hardening
* **Hybrid Retrieval:** Utilizes Weaviate's native hybrid search, combining dense vector semantic search with BM25 keyword matching.
* **Pairwise Re-ranking:** Implements a local cross-encoder model to re-score query-chunk pairs, drastically improving precision.
* **Refusal Guardrails:** The system is explicitly prompted (via version-controlled YAML configs) to decline answering if the retrieved chunks lack sufficient evidence, preventing hallucination.

### Phase 3: Evaluation & CI/CD
* **Golden Dataset:** Evaluated against a curated JSON dataset of verified QA pairs.
* **LLM-as-a-Judge:** Uses Ragas to mathematically score the system's **Faithfulness** (ensuring all claims in the generated answer trace back to the retrieved context).
* **CI/CD Ready:** The evaluation script acts as a CI gate, failing the build automatically if the Faithfulness score drops below 0.8 (80%).

## Project Structure

```text
tft-rag-system/
├── configs/
│   └── prompts/
│       ├── v1_generation.yaml     # Baseline prompt
│       └── v2_generation.yaml     # Production prompt with refusal guardrails
├── data/
│   ├── raw/                       # Scraped HTML
│   ├── processed/                 # Cleaned Markdown and chunked data
│   └── eval/
│       └── golden_dataset.json    # Ground truth QA pairs
├── src/
│   ├── scraper/                   # HTML fetching and Markdown parsing
│   ├── ingestion/                 # Text splitting and Weaviate batch imports
│   ├── retrieval/                 # Hybrid search and Cross-Encoder reranking
│   └── pipeline/                  # LangChain orchestration and formatting
├── eval/
│   └── run_eval.py                # Ragas faithfulness evaluation script
├── docker-compose.yml             # Local Weaviate instance with volume persistence
└── requirements.txt
```

## Getting Started

### 1. Prerequisites
* Python 3.10+
* Docker Desktop (for Weaviate)
* A free [Google AI Studio](https://aistudio.google.com/) API key.

### 2. Setup Environment
```bash
# Clone the repo
git clone https://github.com/yourusername/tft-rag-system.git
cd tft-rag-system

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_google_api_key_here
```

### 4. Start the Vector Database
Spin up the local Weaviate container (data is persisted to a local docker volume):
```bash
docker compose up -d
```

## Usage

**1. Ingest Data:**
Generate local embeddings and load chunks into Weaviate:
```bash
python -m src.ingestion.vector_store
```

**2. Run the Pipeline:**
Test the production hybrid-retrieval pipeline with guardrails:
```bash
python -m src.pipeline.chain
```

**3. Run Quality Evaluation:**
Calculate the Faithfulness metric using Ragas and the Golden Dataset:
```bash
python -m eval.run_eval
```