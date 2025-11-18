from flask import Flask, request, jsonify
from flask_cors import CORS
from faster_whisper import WhisperModel
import os

app = Flask(__name__)
CORS(app)

# Load model once (MUCH faster and avoids crashes)
MODEL_CACHE = {}

def get_model(size):
    if size not in MODEL_CACHE:
        MODEL_CACHE[size] = WhisperModel(size, device="cpu", compute_type="int8")
    return MODEL_CACHE[size]


@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file provided"}), 400

        audio_file = request.files['audio']
        model_size = request.form.get('model_size', 'base')
        language = request.form.get('language', 'auto')

        # Save temporarily
        temp_path = f"temp_{audio_file.filename}"
        audio_file.save(temp_path)

        # Load model
        model = get_model(model_size)

        # Whisper expects None for auto
        lang = None if language == "auto" else language

        segments, info = model.transcribe(
            temp_path,
            beam_size=5,
            language=lang
        )

        result = []
        for s in segments:
            result.append({
                'start': s.start,
                'end': s.end,
                'text': s.text
            })

        os.remove(temp_path)
        return jsonify({"segments": result, "language": info.language})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
