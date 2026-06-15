import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpointEmbeddings

load_dotenv()

# Map HUGGING_FACE_API_KEY to HUGGINGFACEHUB_API_TOKEN if present
if "HUGGING_FACE_API_KEY" in os.environ and "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HUGGING_FACE_API_KEY"]

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
)

persist_directory = "./.chroma"

if not os.path.exists(persist_directory):
    urls = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
        "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    ]

    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)

    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=embeddings,
        persist_directory=persist_directory,
    )
    retriever = vectorstore.as_retriever()
else:
    retriever = Chroma(
        collection_name="rag-chroma",
        persist_directory=persist_directory,
        embedding_function=embeddings,
    ).as_retriever()