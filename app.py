import os
import numpy as np
import librosa
import noisereduce as nr
import soundfile as sf
import tensorflow as tf
import pickle
import speech_recognition as sr
from flask import Flask, render_template, request, jsonify
from gtts import gTTS

app = Flask(__name__)
# 📌 Ensure model folder exists
MODEL_DIR = "model"
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# 📌 Load Trained Bi-LSTM Model
MODEL_PATH = os.path.join(MODEL_DIR, "speech_text_emotion_model.h5")
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"🚨 ERROR: Model file not found at {MODEL_PATH}")
model = tf.keras.models.load_model(MODEL_PATH)

# 📌 Load Label Encoders
LABEL_ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")
TEXT_LABEL_ENCODER_PATH = os.path.join(MODEL_DIR, "text_label_encoder.pkl")

with open(LABEL_ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)
with open(TEXT_LABEL_ENCODER_PATH, "rb") as f:
    text_label_encoder = pickle.load(f)

# 📌 Load TF-IDF Vectorizer and NLP Classifier
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
NLP_CLASSIFIER_PATH = os.path.join(MODEL_DIR, "nlp_classifier.pkl")

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)
with open(NLP_CLASSIFIER_PATH, "rb") as f:
    nlp_classifier = pickle.load(f)

# 📌 Emotion to Emoji Mapping
EMOTION_TO_EMOJI = {
    "Neutral": "😐",
    "Calm": "😌",
    "Happy": "😊",
    "Sad": "😢",
    "Angry": "😠",
    "Fearful": "😨",
    "Disgust": "🤢",
    "Surprised": "😲"
}

# 📌 Extract Features from Audio
def extract_features(file_path):
    try:
        y, sr = librosa.load(file_path, sr=22050)
        y, _ = librosa.effects.trim(y, top_db=25)  # Remove silence
        y = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.9)

        if len(y) < sr:
            print(f"❌ ERROR: Audio too short after processing.")
            return None
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"❌ ERROR: Feature Extraction Failed -> {e}")
        return None

import subprocess
def convert_audio_to_wav(input_path):
    """Convert any audio file to PCM WAV format using FFmpeg."""
    output_path = input_path.replace(".wav", "_converted.wav")  # Save new file
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", output_path
        ], check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR: FFmpeg Conversion Failed -> {e}")
        return None

# 📌 Convert Speech to Text
def speech_to_text(file_path):
    recognizer = sr.Recognizer()
    # Convert to PCM WAV if needed
    converted_path = convert_audio_to_wav(file_path)
    if not converted_path:
        return "Error converting audio file"
    try:
        with sr.AudioFile(converted_path) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("⚠️ ERROR: Could not understand the recorded audio.")
        return "Could not understand audio"
    except sr.RequestError:
        print("⚠️ ERROR: Speech recognition API unavailable.")
        return "API unavailable"
# 📌 Predict Emotion from Audio & Text
def predict_emotion(file_path):
    features = extract_features(file_path)
    if features is None:
        return "Error extracting audio features", "", ""
    features = np.expand_dims(features, axis=0)
    features = np.expand_dims(features, axis=-1)
    audio_prediction = model.predict(features)
    audio_emotion = label_encoder.inverse_transform([np.argmax(audio_prediction)])[0]
    text = speech_to_text(file_path)
    text_emotion = "unknown"
    if text.strip():
        try:
            text_features = vectorizer.transform([text])
            text_prediction = nlp_classifier.predict(text_features)
            text_emotion = text_label_encoder.inverse_transform(text_prediction)[0]
        except Exception as e:
            print(f"⚠️ ERROR: NLP Prediction Failed -> {e}")
    final_emotion = audio_emotion if audio_emotion == text_emotion else audio_emotion
    return final_emotion, EMOTION_TO_EMOJI.get(final_emotion, "❓")

# 📌 Convert Detected Emotion to Speech
def text_to_speech(emotion, output_path="static/output_voice.mp3"):
    spoken_text = f"Emotion is {emotion}."
    tts = gTTS(text=spoken_text, lang="en", slow=False)
    tts.save(output_path)
    return output_path

# 📌 Routes
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    emotion, emoji = predict_emotion(file_path)
    voice_file = text_to_speech(emotion)
    return jsonify({
        "emotion": emotion,
        "emoji": emoji,
        "audio": voice_file
    })

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
