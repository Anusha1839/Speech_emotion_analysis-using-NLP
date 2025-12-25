import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Sample text dataset and emotions (Replace with actual dataset if available)
text_samples = [
    "I am happy today", "I feel so sad", "This is frustrating", "I am very angry",
    "What a joyful day", "I am afraid of the dark", "This is disgusting", "I am surprised"
]
emotion_labels = ["happy", "sad", "angry", "angry", "happy", "fearful", "disgust", "surprised"]

# Load existing vectorizer (Make sure `vectorizer.pkl` exists)
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Convert text to TF-IDF features
X_text = vectorizer.transform(text_samples)

# Encode emotion labels
label_encoder_text = LabelEncoder()
y_text = label_encoder_text.fit_transform(emotion_labels)

# Train NLP classifier
nlp_classifier = LogisticRegression()
nlp_classifier.fit(X_text, y_text)

# Save NLP classifier
with open("model/nlp_classifier.pkl", "wb") as f:
    pickle.dump(nlp_classifier, f)

# Save Label Encoder for text emotions
with open("model/text_label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder_text, f)

print("✅ nlp_classifier.pkl and text_label_encoder.pkl have been successfully created!")
