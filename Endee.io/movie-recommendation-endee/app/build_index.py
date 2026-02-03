import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load dataset
df = pd.read_csv("data/movies.csv")

# Create embeddings
embeddings = model.encode(df["plot"].tolist())

# Save vectors locally (simulating vector DB storage)
np.save("movie_vectors.npy", embeddings)
df[["id", "title"]].to_csv("movie_metadata.csv", index=False)

print("✅ Movie embeddings created and stored")
