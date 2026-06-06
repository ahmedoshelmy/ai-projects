import os
from dotenv import load_dotenv

load_dotenv()

import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from pinecone import Pinecone, ServerlessSpec
from langsmith import traceable

# --- Config ---
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gpt-oss:120b-cloud"
INDEX_NAME = "blog-analyzer"
DIMENSION = 384
BLOG_URL = "https://lilianweng.github.io/posts/2023-06-23-agent/"

# --- Embeddings (HuggingFace free API) ---
embeddings = HuggingFaceEndpointEmbeddings(
    model=EMBEDDING_MODEL,
    huggingfacehub_api_token=os.environ["HUGGING_FACE_API_KEY"],
)

# --- LLM (Ollama) ---
llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0,
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")}},
)


# --- Pinecone index setup ---
def get_or_create_index() -> PineconeVectorStore:
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    existing = [idx.name for idx in pc.list_indexes()]
    if INDEX_NAME not in existing:
        print(f"Creating Pinecone index '{INDEX_NAME}'...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        print("Index created.")
    else:
        print(f"Using existing Pinecone index '{INDEX_NAME}'.")
    return PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)


# --- Ingest: load → chunk → embed → store ---
def ingest(url: str) -> PineconeVectorStore:
    print(f"\n[1/3] Loading blog from: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    docs = [Document(page_content=text, metadata={"source": url})]
    print(f"      Loaded {len(docs)} document(s).")

    print("[2/3] Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    print(f"      {len(chunks)} chunks created.")

    print("[3/3] Embedding & storing to Pinecone...")
    vector_store = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name=INDEX_NAME,
    )
    print(f"      Done. {len(chunks)} chunks stored in index '{INDEX_NAME}'.\n")
    return vector_store


# --- RAG chain ---
def build_rag_chain(vector_store: PineconeVectorStore):
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    def retrieve_and_print(question: str) -> list:
        docs = retriever.invoke(question)
        print(f"\n--- Retrieved {len(docs)} chunk(s) ---")
        for i, doc in enumerate(docs, 1):
            print(f"[{i}] {doc.page_content[:200].strip()}...")
        print("---")
        return docs

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant that answers questions strictly based on blog content.\n"
            "Use only the provided context. If the answer is not in the context, say so clearly.\n\n"
            "Context:\n{context}",
        ),
        ("human", "{question}"),
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": RunnableLambda(retrieve_and_print) | RunnableLambda(format_docs), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


# --- Main ---
@traceable(name="Blog RAG")
def main():
    get_or_create_index()
    vector_store = ingest(BLOG_URL)
    chain = build_rag_chain(vector_store)

    print("Blog RAG ready. Ask questions (type 'exit' to quit).\n")
    while True:
        question = input("Question: ").strip()
        if not question or question.lower() in ("exit", "quit"):
            break
        answer = chain.invoke(question)
        print(f"\nAnswer: {answer}\n")


if __name__ == "__main__":
    main()

