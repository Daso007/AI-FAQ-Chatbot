# AI-Powered FAQ Chatbot

This is a Retrieval-Augmented Generation (RAG) powered chatbot that can answer questions based on a specific, private knowledge source. It uses a FAISS vector store for efficient semantic search and a Llama 3 LLM (via Groq) for natural language generation.

## Key Features

- **Data Ingestion:** Scrapes text from any public URL.
- **Semantic Search:** Uses sentence-transformer embeddings to understand the meaning of questions, not just keywords.
- **Accurate Generation:** Leverages RAG to ground the LLM's answers in the provided context, preventing hallucination.
- **Interactive:** Provides a command-line interface for real-time Q&A.

## Technology Stack

- **Framework:** LangChain
- **LLM:** Llama 3 (via Groq)
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Store:** FAISS (Facebook AI Similarity Search)
- **Programming Language:** Python

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/Your-Repository-Name.git
    cd Your-Repository-Name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate # On Mac/Linux
    .\.venv\Scripts\activate  # On Windows
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file)*

4.  **Set up your Groq API Key:**
    Sign up for a free key at `https://console.groq.com/`. Then, set it as an environment variable.
    ```bash
    export GROQ_API_KEY="YOUR_API_KEY_HERE" # On Mac/Linux
    set GROQ_API_KEY="YOUR_API_KEY_HERE"   # On Windows
    ```

5.  **Run the application:**
    ```bash
    # First, run the setup scripts to build the knowledge base
    python step1_scrape_data.py
    python step2_chunk_data.py
    python step3_create_vector_store.py

    # Then, run the main chatbot
    python step4_ask_the_bot.py
    ```
