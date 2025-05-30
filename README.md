# PDF Question Answering with Web Scraping and LangChain

This project demonstrates how to scrape text from a webpage, convert it into a PDF, and build a question-answering system using LangChain with and without retrieval augmentation.

## Overview

- **Web scraping:** Extracts textual data from a webpage (Wikipedia) using Python.
- **PDF generation:** Saves the scraped text as a nicely formatted PDF.
- **PDF processing:** Loads and splits the PDF content into smaller chunks.
- **Embeddings and vector store:** Creates semantic embeddings and stores them in a FAISS vector database.
- **Language model:** Uses an Ollama large language model (LLM) for answering questions directly and with retrieval-augmented generation (RAG).
- **Interactive Q&A:** Allows users to ask questions about the PDF content and get answers both from the LLM alone and from the combined retrieval + LLM pipeline.
