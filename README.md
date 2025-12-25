# Speech_emotion_analysis-using-NLP
## Project Overview
- Speech Emotion Analyzer is a machine learning and NLP-based system designed to detect and classify human emotions from speech
- The system analyzes both acoustic and textual features to accurately identify emotions
- It supports real-time emotion detection through audio recording or audio file upload
- This project is developed as part of the Bachelor of Technology (B.Tech) curriculum in AI & ML,the output is defined in 3 formats voice,emoji, and text.

# Objectives of the Project
+ Convert speech input into text using Automatic Speech Recognition (ASR)
+ Extract meaningful linguistic and acoustic features from speech
+ Classify emotions such as Happy, Sad, Angry, Fearful, Neutral, Calm, Disgust, and Surprised
+ Build a real-time emotion recognition system with a simple web interface
+ Improve human–computer interaction using emotion-aware AI systems

# Problem Definition
- Traditional text-based sentiment analysis fails to capture emotions expressed through tone, pitch, and speech patterns
- Speech emotion recognition is challenging due to speech-to-text errors, background noise, speaker variability, and overlapping emotions
- This project addresses these challenges using NLP, machine learning, and deep learning models

# Proposed System
+ Combines audio signal processing and NLP-based text analysis
+ Uses deep learning models like CNN, LSTM, Bi-LSTM, BERT, and Wav2Vec 2.0
+ Supports real-time emotion classification with low latency
+ Displays emotion output in text, emoji, and audio formats

# Methodology
- Speech Input
  + Record audio or upload an audio file
- Preprocessing
  + Noise removal
  + Silence removal
  + Normalization
- Feature Extraction
  + Acoustic features such as MFCCs, Pitch, Chroma, and Spectrograms
  + Textual features such as TF-IDF, Word2Vec, and BERT embeddings
- Emotion Classification
  + Machine Learning models like SVM and Random Forest
  + Deep Learning models like CNN, LSTM, Bi-LSTM, and Transformers
- Output Generation
  + Emotion displayed as text, emoji, and audio playback

# Dataset Used
- RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)
+ Emotions covered - Neutral, Calm, Happy,Sad,Angry, Fearful, Disgusted,Surprised
+ Total files: 2452
+ Audio format: .wav
+ Language: English
+ Dataset URL: https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio

# Technologies Used
- Python 3.x
- Librosa
- NumPy
- Pandas
- Scikit-learn
- TensorFlow / Keras
- NLTK
- Matplotlib
+ Flask
+ HTML
+ CSS
+ JavaScript
+ VS Code
+ Jupyter Notebook

# Hardware Requirements
- Processor: Intel i7 or AMD Ryzen 7 or higher
- RAM: Minimum 16 GB (32 GB recommended)
- GPU: NVIDIA RTX 3060 or higher
- Storage: 512 GB SSD
- Microphone for real-time speech input

# Results
+ Achieved approximately 92% accuracy using deep learning models
+ Multimodal approach performs better than single-modal systems
+ Clear emotions such as Happy, Angry, and Sad are classified with high accuracy
+ Subtle emotions require further improvement
  ![WhatsApp Image 2025-12-25 at 18 05 29_a54cddf0](https://github.com/user-attachments/assets/6eeb16d3-ec7e-4700-a651-86488c091f67)
  ![WhatsApp Image 2025-12-25 at 18 05 29_14223242](https://github.com/user-attachments/assets/29f4a77e-fdf6-40ea-8041-65cdffff9232)
  ![WhatsApp Image 2025-12-25 at 18 05 29_55c8fc8c](https://github.com/user-attachments/assets/90ea5112-1fc3-4cdf-94c9-32ac99ebda9c)


# Limitations
+ Language dependent and mainly focused on English
+ Difficulty in detecting mixed and subtle emotions
+ Performance affected by background noise
+ Requires large and high-quality labeled datasets
+ High computational cost for real-time processing

# Future Scope
- Multi-label emotion classification
- Multilingual emotion recognition
- Lightweight models for mobile and edge devices
- Integration with facial expression and physiological signals
- Bias reduction and ethical AI improvements
- Cloud-based API deployment

# Applications
+ Customer service sentiment analysis
+ Virtual assistants
+ Mental health monitoring
+ Call center analytics
+ Human–computer interaction
+ Emotion-aware AI systems

# Project Team
- Gudibanda Sirisha
- Gurijala Swathi
- Karina Yadav
- K. E. Dhanusha
- Mandala Dhanush

# Institution
+ Department of Artificial Intelligence and Machine Learning
+ Malla Reddy University, Hyderabad
+ Academic Year: 2025
