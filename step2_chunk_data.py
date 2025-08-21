from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def chunk_data(file_path="scraped_faq.txt"):
    """
    Reads text from a file and splits it into chunks.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None 
    
    with open(file_path, 'r', encoding = 'utf-8') as f:
        text = f.read()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )

    chunks = text_splitter.split_text(text)

    return chunks 

if __name__ == "__main__":
    text_chunks = chunk_data()

    if text_chunks:
        print("--- SUCCESSFULLY CHUNKED THE DATA ---")
        print(f"Total number of chunks created: {len(text_chunks)}")

        print("\n--- PREVIEW OF THE FIRST CHUNK ---")
        print(text_chunks[0])

        print("\n--- PREVIEW OF THE SECOND CHUNK (note the overlap) ---")
        print(text_chunks[1])