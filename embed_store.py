import json
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# Load chunked data
with open(r"C:\Users\gamid\Desktop\Social-Media-RAG\data\chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Convert chunks to LangChain Documents
docs = [
    Document(
        page_content=chunk["text"],
        metadata={
            "post_id": chunk["post_id"],
            "subreddit": chunk["subreddit"]
        }
    ) for chunk in chunks
]

# Initialize HuggingFace Embeddings (without sentence-transformers)
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",  # lightweight & accurate
    model_kwargs={'device': 'cpu'}  # or 'cuda' if you have GPU
)

# Store in Chroma
vectordb = Chroma.from_documents(docs, embedding=embedding, persist_directory="./chroma_db")
vectordb.persist()

print("✅ Vector DB stored successfully with HuggingFace embeddings!")
