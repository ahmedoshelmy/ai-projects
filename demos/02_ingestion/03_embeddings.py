import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from shared_utils import load_env_from_project, get_embeddings
from dotenv import load_dotenv

load_env_from_project()

# Using HuggingFace API embeddings
embeddings = get_embeddings("BAAI/bge-small-en-v1.5")















# embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# # single text
# text = "This is a sample text to be embedded."
# embedding = embeddings.embed_query(text)
# # print(f"Embedding for single text: {embedding}")

# print(len(embedding))  # Should print 1536 for text-embedding-3-small


# # multiple texts
# embeds = embeddings.embed_documents(
#     ["This is the first document.", "This is the second document."]
# )
# print(f"Embeddings for multiple texts: {embeds}")
# print(f"Number of embeddings returned: {len(embeds)}")  # Should print 2
# print(
#     f"Length of each embedding: {len(embeds[0])}"
# )  # Should print 1536 for text-embedding-3-small
