from step2_chunk_data import chunk_data

from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store():
    """
    Creates a FAISS vector store from text chunks and saves it to a local folder.

    """

    chunks = chunk_data()
    if not chunks:
        print("No chunks were created. Halting execution.")
        return
    
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceBgeEmbeddings(model_name=model_name)

    print("--- Embedding model loaded ---")

    print("--- Creating vector store... (This may take a moment) ---")

    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)

    vector_store.save_local("faiss_index")

    print("--- Vector store created and saved to 'faiss_index' folder! ---")

if __name__ == "__main__":
    create_vector_store()

    print("\n--- Running a test query ---")

    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    db = FAISS.load_local("faiss_index", embeddings , allow_dangerous_deserialization=True)

    query = "How am I billed for using Amazon S3?"

    docs = db.similarity_search(query, k =3 )

    print(f"\n--- Top 3 most relevant chunks for the query: '{query}' ---")
    for i, doc in enumerate(docs):
        print(f"\n--- Result {i+1} ---")
        print(doc.page_content)

