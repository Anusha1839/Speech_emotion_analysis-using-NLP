import pickle
from sklearn.preprocessing import LabelEncoder

# Define the emotion labels from RAVDESS dataset (or adjust based on your dataset)
emotion_labels = ["Neutral", "Calm", "Happy", "Sad", "Angry", "Fearful", "Disgust", "Surprised"]

# Initialize and fit LabelEncoder
label_encoder = LabelEncoder()
label_encoder.fit(emotion_labels)

# Save label encoder to file
with open("model/label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("✅ label_encoder.pkl has been successfully created!")
