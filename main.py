from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA


loader = PyPDFLoader("output.pdf")
pages = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
docs = text_splitter.split_documents(pages)


embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


vectorDB = FAISS.from_documents(docs, embedding_model)



retriever = vectorDB.as_retriever()


llm = OllamaLLM(model="gemma:2b")


qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)


print("Ask a question about the PDF. Type !Bye to exit.\n")
while True:
    question = input("Question: ")
    if question.strip().lower() == "!bye":
        print("Goodbye!")
        break

    print("\n  Without RAG:")
    direct_response = llm.invoke(question)
    print(direct_response)

    print("\n  With RAG:")
    rag_response = qa_chain.invoke(question)
    print("Answer:", rag_response["result"], "\n")