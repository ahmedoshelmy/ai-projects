from dotenv import load_dotenv
import os

load_dotenv()

from langchain_huggingface import HuggingFaceEndpointEmbeddings

# Free model via HuggingFace Inference API
# sentence-transformers/all-MiniLM-L6-v2 → 384 dimensions, cosine similarity
MODEL = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEndpointEmbeddings(
    model=MODEL,
    huggingfacehub_api_token=os.environ["HUGGING_FACE_API_KEY"],
)

texts = ["Hello world", "RAG systems are powerful"]
vectors = embeddings.embed_documents(texts)

print(f"Model:       {MODEL}")
print(f"Dimensions:  {len(vectors[0])}")
print(f"Num vectors: {len(vectors)}")
print(f"First 5 values of vector[0]: {vectors[0][:5]}")
print()
print("--- Pinecone config ---")
print(f"dimension:  {len(vectors[0])}")
print(f"metric:     cosine")
