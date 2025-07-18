# Semantic Similarity Search

## 📖 Introduction

This project demonstrates how to use [Sentence Transformers](https://www.sbert.net/) to compute sentence embeddings and analyze semantic similarity among a collection of sentences. It includes code to calculate a similarity matrix and to find the closest matching sentence to a given query.

---

## 🚀 Overview

- **Embeds a list of 30 diverse sentences** using the `all-MiniLM-L6-v2` model.
- **Computes a cosine similarity matrix** between all pairs of sentences.
- **Provides a function** to find and display the closest match for any new input sentence based on semantic similarity.
- Useful for **semantic search**, **chatbot retrieval**, and **natural language understanding** demos.

---

## Visual Diagram

```mermaid
graph TD
    A[Start: List of sentences] --> B[Generate embeddings using SentenceTransformer]
    B --> C[Calculate cosine similarity matrix]
    C --> D[Display semantic similarity results]
    D --> E{User provides a query?}
    E -- Yes --> F[Embed query sentence]
    F --> G[Find closest match in sentence set]
    G --> H[Display most similar sentence]
    E -- No --> I[End]


