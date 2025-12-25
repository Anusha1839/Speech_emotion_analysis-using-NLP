let recorder, audioChunks = [];

// ✅ Ensure elements exist before accessing them
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("processing").style.display = "none";
    document.getElementById("result").style.display = "none";
});

// Toggle between upload and record sections
function toggleInput() {
    let option = document.getElementById("option").value;
    document.getElementById("uploadSection").style.display = option === "upload" ? "block" : "none";
    document.getElementById("recordSection").style.display = option === "record" ? "block" : "none";
    clearResults();
}

// ✅ Show "Processing..." animation
function showProcessing() {
    let processingDiv = document.getElementById("processing");
    if (processingDiv) processingDiv.style.display = "block";

    let resultDiv = document.getElementById("result");
    if (resultDiv) resultDiv.style.display = "none";
}

// ✅ Hide "Processing..." animation
function hideProcessing() {
    let processingDiv = document.getElementById("processing");
    if (processingDiv) processingDiv.style.display = "none";
}

// ✅ Clear results
function clearResults() {
    let emotionText = document.getElementById("emotionText");
    let emotionEmoji = document.getElementById("emotionEmoji");
    let emotionAudio = document.getElementById("emotionAudio");
    let resultDiv = document.getElementById("result");

    if (emotionText) emotionText.innerText = "";
    if (emotionEmoji) emotionEmoji.innerText = "";
    if (emotionAudio) {
        emotionAudio.src = "";
        emotionAudio.style.display = "none";
    }
    if (resultDiv) resultDiv.style.display = "none";
}

// ✅ Clear uploaded file
function clearUpload() {
    let fileInput = document.getElementById("audioFile");
    if (fileInput) fileInput.value = "";
    clearResults();
}

// ✅ Upload Audio File
function uploadAudio() {
    let fileInput = document.getElementById("audioFile");
    if (!fileInput || fileInput.files.length === 0) {
        alert("Please select an audio file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    showProcessing();

    fetch("/predict", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            hideProcessing();
            displayResults(data);
        })
        .catch(error => {
            hideProcessing();
            console.error("Error:", error);
        });
}

// ✅ Start Recording
function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        recorder = new MediaRecorder(stream);
        audioChunks = [];

        recorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        recorder.start();

        document.getElementById("recordButton").disabled = true;
        document.getElementById("stopButton").disabled = false;
        document.getElementById("predictButton").disabled = true;
        document.getElementById("clearRecordButton").disabled = true;

        clearResults();
    }).catch(error => console.error("Error:", error));
}

// ✅ Stop Recording
function stopRecording() {
    recorder.stop();
    recorder.onstop = () => {
        let audioBlob = new Blob(audioChunks, { type: "audio/wav" });
        let audioUrl = URL.createObjectURL(audioBlob);

        let audioElement = document.getElementById("recordedAudio");
        if (audioElement) {
            audioElement.src = audioUrl;
            audioElement.style.display = "block";
        }

        // ✅ Enable Predict & Clear Buttons
        document.getElementById("predictButton").disabled = false;
        document.getElementById("clearRecordButton").disabled = false;
    };

    document.getElementById("stopButton").disabled = true;
}

// ✅ Detect Emotion from Recorded Audio
function predictRecordedAudio() {
    if (audioChunks.length === 0) {
        alert("No recorded audio found. Please record first.");
        return;
    }

    let audioBlob = new Blob(audioChunks, { type: "audio/wav" });
    let file = new File([audioBlob], "recorded_audio.wav", { type: "audio/wav" });

    let formData = new FormData();
    formData.append("file", file);

    showProcessing();

    fetch("/predict", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            hideProcessing();
            displayResults(data);
        })
        .catch(error => {
            hideProcessing();
            console.error("Error:", error);
        });
}

// ✅ Clear Recorded Audio
function clearRecording() {
    audioChunks = [];
    let audioElement = document.getElementById("recordedAudio");
    if (audioElement) audioElement.style.display = "none";

    document.getElementById("predictButton").disabled = true;
    document.getElementById("recordButton").disabled = false;
    document.getElementById("clearRecordButton").disabled = true;
    clearResults();
}

// ✅ Display Results
function displayResults(data) {
    let emotionText = document.getElementById("emotionText");
    let emotionEmoji = document.getElementById("emotionEmoji");
    let emotionAudio = document.getElementById("emotionAudio");
    let resultDiv = document.getElementById("result");

    if (emotionText) emotionText.innerText = data.emotion;
    if (emotionEmoji) emotionEmoji.innerText = data.emoji;

    if (emotionAudio) {
        emotionAudio.src = data.audio;
        emotionAudio.style.display = "block";
    }

    if (resultDiv) resultDiv.style.display = "block";
}
