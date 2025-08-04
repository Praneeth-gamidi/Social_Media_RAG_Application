# RAG-based Question Answering App using LangChain and Streamlit

This is a Retrieval-Augmented Generation (RAG) based Question Answering app built using:

- **LangChain**
- **Sentence Transformers** (`all-MiniLM-L6-v2`)
- **Chroma VectorDB**
- **HuggingFace Transformers** (`google/flan-t5-large`)
- **Streamlit**

## Features

- Embeds documents into a vector store
- Retrieves relevant chunks based on user questions
- Uses `flan-t5-large` to generate natural language answers
- Provides source documents for transparency
- Clean command-line interface (CLI) and can be extended to Streamlit UI

 How to Run Locally

1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run app.py
📁 Folder Structure
bash
Copy
Edit
├── app.py               # Streamlit frontend
├── rag.py               # LangChain + RAG backend logic
├── chroma_db/           # Chroma vector store files
├── requirements.txt     # Python dependencies
└── README.md
🧠 Model Info
Embedding Model: sentence-transformers/all-MiniLM-L6-v2

LLM: google/flan-t5-large
