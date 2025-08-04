import streamlit as st
from rag import generate_response

st.set_page_config(page_title="Local RAG App", layout="wide")
st.title("💬 Social Media RAG Application")

query = st.text_input("Ask your question:")
if query:
    with st.spinner("Generating answer..."):
        answer, sources = generate_response(query)
        st.write("### 📌 Answer:")
        st.success(answer)

        st.write("### 📁 Sources:")
        for src in sources:
            st.write(f"- {src}")
