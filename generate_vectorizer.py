import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample text dataset (you can replace this with actual dataset)
text_samples = [
    "I am happy today", "I feel so sad", "This is frustrating", "I am very angry",
    "What a joyful day", "I am afraid of the dark", "This is disgusting", "I am surprised"
]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
vectorizer.fit(text_samples)

# Save the vectorizer to a file
with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ vectorizer.pkl has been successfully created!")
