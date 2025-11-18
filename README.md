# 🎙️ Audio Transcription Tool

### *Real-time audio-to-text system using Flask + Faster Whisper + HTML/JS*

<p align="center">
  <img src="banner.png" alt="Project Banner" width="80%" />
</p>

<p align="center">
  <strong>Fast • Accurate • Lightweight • Exportable Transcriptions</strong>
</p>

---

## 🏷️ Badges

<p align="center">

<img src="https://img.shields.io/badge/Python-3.9+-blue.svg" />
<img src="https://img.shields.io/badge/Flask-API-green.svg" />
<img src="https://img.shields.io/badge/Faster--Whisper-ASR-purple.svg" />
<img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange.svg" />
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" />

</p>

---

# 🚀 Overview

This project provides a complete **speech-to-text transcription pipeline**, featuring:

* A **Python Flask API** for audio processing
* A **modern web UI** for uploading and transcribing audio
* The **Faster-Whisper model** for fast & accurate transcription
* Export options for **PDF**, **Word (.doc)**, and **TXT**
* Supports **multiple model sizes** and **language auto-detection**

---

# 🧰 THM — Tools, Technologies & Methods

### **Tools**

* Flask (Python)
* Faster-Whisper
* FFmpeg
* jsPDF
* DocxTemplater
* FileSaver.js

### **Technologies**

* REST API
* Multipart file upload
* Cross-origin communication (CORS)
* Whisper model inference

### **Methods**

* CPU/GPU accelerated speech recognition
* Timestamp segmentation
* Language auto-detection
* Client-side file export
* Single-pass JSON serialization

This section clearly shows what powers the project at a technical level.

---

# ✨ Features

### 🔊 **Frontend**

* Clean drag & drop audio uploader
* Model size selector (tiny → large-v3)
* Language selector (or auto-detect)
* Loading animation
* Timestamped, formatted transcript
* Export to:

  * 📄 PDF
  * 📝 Word
  * 💾 TXT
* Copy transcript to clipboard

### 🧠 **Backend**

* Fast transcription using Faster-Whisper
* Loads models *once* for speed
* Graceful error handling
* CORS enabled
* Supports any model size
* Supports CPU & GPU environments

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

---

## 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

---

## 3️⃣ Install Dependencies

```bash
pip install flask flask-cors faster-whisper
```

Ensure FFmpeg is installed:

### Linux

```bash
sudo apt install ffmpeg
```

### macOS

```bash
brew install ffmpeg
```

### Windows

Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

---

## 4️⃣ Start the Backend API

```bash
python transcribe_flask.py
```

Runs at:

```
http://127.0.0.1:5000
```

---

## 5️⃣ Open the Frontend

Open the file locally:

```
transcribe_frontend.html
```

No server needed for the UI.

---

# 🔗 API Documentation

### ▶️ POST `/transcribes`

Upload audio, receive JSON transcript.

#### **Form Data**

| Key          | Type | Required | Description                         |
| ------------ | ---- | -------- | ----------------------------------- |
| `audio`      | file | Yes      | Audio file                          |
| `model_size` | text | No       | tiny, base, small, medium, large-v3 |
| `language`   | text | No       | auto, en, fr, es, etc.              |

#### **Example Response**

```json
{
  "segments": [
    {
      "start": 0.0,
      "end": 4.2,
      "text": "Hello world"
    }
  ],
  "language": "en"
}
```

---

# 🖼️ Screenshots (optional)

```
![UI Upload](images/ui_upload.png)
![Transcription](images/transcription.png)
```

---

# 🧪 Troubleshooting

### ❗ “Error during transcription”

Usually caused by:

* Flask returned **HTML instead of JSON**
* FFmpeg missing
* Model not found
* Backend crashed while transcribing

Check terminal logs for error messages.

---

# 🛣️ Roadmap

* Real-time streaming transcript (WebSockets)
* Speaker identification
* Dark Mode UI
* Full frontend framework version (React)
* GPU-accelerated Docker deployment

---

# 🤝 Contributing

PRs welcome!
Open an issue for feature requests.

---

# 📄 License

MIT License – free to use, modify, and distribute.

---

# 🎉 Final Note

This project is designed to be simple, fast, and extendable.

