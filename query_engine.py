from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader

# Load the same embedding model used before
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the persisted Chroma DB
vectordb = Chroma(persist_directory="chroma_db", embedding_function=embedding_model)

# Ask the user for a query
query = input("Enter your question: ")

# Perform similarity search
results = vectordb.similarity_search(query, k=3)

# Print the most relevant chunks
print("\nTop Matching Chunks:\n" + "-"*40)
for i, res in enumerate(results, 1):
    print(f"Result {i}:\n{res.page_content}\n")
