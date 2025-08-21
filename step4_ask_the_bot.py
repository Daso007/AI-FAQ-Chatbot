from langchain_community.vectorstores import FAISS 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def format_docs(docs):
    """A helper function to format the retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)


def setup_rag_chain():
    """
    Sets up the full RAG (Retrieval-Augmented Generation) chain.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vector_store = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )


    retriever = vector_store.as_retriever(search_kwargs={"k":3})

    llm = ChatGroq(model = "llama3-8b-8192")

    template = """
    You are an expert technical assistant. Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know. Do not try to make up an answer.
    Keep the answer concise and to the point.
    
    Context: {context}
    
    Question: {question}
    
    Helpful Answer:
    """

    prompt = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain

if __name__ == "__main__":
    try:
        chain = setup_rag_chain()

        print("--- AWS S3 FAQ Bot is Ready ---")
        print("Ask a question. Type 'exit' to quit.")

        while True:
            user_question = input("\nYour Question: ")
            if user_question.lower() == 'exit' :
                break

            print("Bot's Answer: ", end="", flush=True)
            for chunk in chain.stream(user_question):
                print(chunk,end="", flush = True)
            print("\n" + "="*50)

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please ensure your GROQ_API_KEY is set correctly as an environment variable.")    