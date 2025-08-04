import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# ✅ Embedding model
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

# ✅ Load Chroma DB
vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings,
)
retriever = vectordb.as_retriever(search_kwargs={"k": 5})

# ✅ Load local model
generator_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-large",
    tokenizer="google/flan-t5-large",
    max_length=256,
    do_sample=True,
    temperature=0.5
)
llm = HuggingFacePipeline(pipeline=generator_pipeline)

# ✅ QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# ✅ Function to be used by Streamlit
def generate_response(query):
    if not query:
        return "Please enter a question.", []

    result = qa_chain.invoke(query)
    answer = result['result']
    sources = [doc.metadata.get('source', 'Unknown') for doc in result['source_documents']]
    return answer, sources

# ✅ Optional CLI fallback (for testing in terminal)
if __name__ == "__main__":
    print("Ask a question (type 'exit' to quit):")
    while True:
        query = input("\nYour question: ")
        if query.lower() == "exit":
            break
        answer, sources = generate_response(query)
        print("\nAnswer:", answer)
        print("\nSources:")
        for src in sources:
            print("-", src)
