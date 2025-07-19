# Semantic Similarity Search

## 📖 Introduction

This project demonstrates how to use [Sentence Transformers](https://www.sbert.net/) to compute sentence embeddings and analyze semantic similarity among a collection of sentences. It includes code to calculate a similarity matrix and to find the closest matching sentence to a given query.

---

## 🚀 Overview

- **Embeds a list of 30 diverse sentences** using the `all-MiniLM-L6-v2` model.
- **Computes a cosine similarity matrix** between all pairs of sentences.
- **Provides a function** to find and display the closest match for any new input sentence based on semantic similarity.
- Useful for **semantic search**, **chatbot retrieval**, and **natural language understanding** demos.

**Sentence Embedding**

A list of sentences is embedded using the all-MiniLM-L6-v2 model from Sentence Transformers. Each sentence is converted into a fixed-length numerical vector (embedding) that captures its semantic meaning.

<img width="1430" height="582" alt="image" src="https://github.com/user-attachments/assets/700fd544-8f7a-491f-84f7-1815b0839620" />

**Similarity Matrix Calculation**

Cosine similarity is computed for each pair of sentence embeddings. This produces a similarity matrix, which quantifies how semantically close each sentence is to the others. The matrix is printed as a readable report, showing the similarity score between each pair of sentences (values closer to 1 mean higher similarity).

<img width="1413" height="830" alt="image" src="https://github.com/user-attachments/assets/0f36174f-7e9f-48fe-af26-eb9e18ffbf44" />

**Semantic Search / Closest Match**

The function get_closest_match takes a new query sentence, computes its embedding, and compares it to all stored embeddings using cosine similarity. It returns the most semantically similar sentence from the list, demonstrating how the model can retrieve relevant information based on meaning, not just keywords.

<img width="1515" height="780" alt="image" src="https://github.com/user-attachments/assets/8cd3f75e-188b-443a-b469-0e084eb607e0" />



## Visual Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Load pre-trained model<br/>SentenceTransformer('all-MiniLM-L6-v2')]
    B --> C[Define sample sentences (Python list)]
    C --> D[Generate embeddings<br/>model.encode(sentences)]
    D --> E[Print shape and example of embeddings]

    E --> F[Calculate cosine similarity matrix<br/>(cosine_similarity)]
    F --> G[Print semantic similarity matrix<br/>(Upper triangle, readable format)]

    G --> H{Next Step?}
    H -- "Semantic Search" --> I[Input Query Sentence (e.g., 'pubg')]
    I --> J[Encode query sentence<br/>model.encode([sentence])]
    J --> K[Compute cosine similarity<br/>between query and all embeddings]
    K --> L[Find and return<br/>most similar sentence]

    H -- "Stop" --> M([End])
    L --> M




