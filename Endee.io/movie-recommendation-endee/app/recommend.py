import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load stored data
vectors = np.load("movie_vectors.npy")
meta = pd.read_csv("movie_metadata.csv")

def recommend(query, top_k=5):
    query_vec = model.encode([query])
    scores = cosine_similarity(query_vec, vectors)[0]
    top_indices = scores.argsort()[-top_k:][::-1]

    print("\n🎬 Recommended Movies:\n")
    for idx in top_indices:
        print("-", meta.iloc[idx]["title"])

query = input("Describe the movie you want: ")
recommend(query)
