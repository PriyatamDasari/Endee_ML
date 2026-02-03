# Movie Recommendation System using Endee

## 📌 Project Overview
This project implements a **semantic movie recommendation system** using
vector embeddings and similarity search.  
The system recommends movies based on the **meaning of user queries**, not
just keywords.

The project demonstrates how **Endee** can be used as a **vector database**
for storing and searching embeddings in AI/ML applications.

---

## 🎯 Problem Statement
Traditional recommendation systems rely on genres or ratings, which fail to
capture the semantic meaning of user preferences.

The goal of this project is to:
- Convert movie descriptions into vector embeddings
- Perform semantic similarity search
- Recommend relevant movies based on user input

---

## 🧠 System Design / Technical Approach

1. **Dataset**
   - A CSV file containing 50 movies from:
     - Hollywood
     - Bollywood
     - Tollywood
     - Kollywood
   - Each movie has a title and plot description

2. **Embedding Generation**
   - Used `sentence-transformers (all-MiniLM-L6-v2)`
   - Movie plots are converted into numerical vector embeddings

3. **Vector Storage**
   - Embeddings are stored locally to simulate vector database behavior
   - This mirrors how Endee stores vectors internally

4. **Similarity Search**
   - Cosine similarity is used to compare user queries with movie embeddings
   - Top similar movies are returned as recommendations

---

## 🗄️ Role of Endee (Vector Database)

Endee is designed as a **vector database** for:
- Storing embeddings
- Performing fast similarity search
- Supporting AI applications like recommendations and semantic search

In this project:
- Endee is used as the **vector database abstraction**
- The same indexing and search logic is demonstrated locally for simplicity
- In a production setup, embeddings would be stored and queried using an
  Endee server (as per Endee documentation)

This approach keeps the project easy to run while clearly showing how Endee
fits into the system architecture.

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
