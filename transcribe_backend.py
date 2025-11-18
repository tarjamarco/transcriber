

from faster_whisper import WhisperModel
import sys
import os

def transcribe_audio(audio_file, model_size="base", device="cpu"):
    
    # Check if file exists
    if not os.path.exists(audio_file):
        print(f"Error: File '{audio_file}' not found!")
        return
    
    print(f"Loading Faster Whisper model ({model_size})...")
    print(f"Using device: {device}")
    
    # Initialize model
    model = WhisperModel(model_size, device=device, compute_type="int8")
    
    print(f"\nTranscribing: {audio_file}")
    print("-" * 50)
    
    # Transcribe audio
    segments, info = model.transcribe(audio_file, beam_size=5)
    
    print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})\n")
    
    # Collect and display transcription
    full_text = []
    
    for segment in segments:
        timestamp = f"[{segment.start:.2f}s -> {segment.end:.2f}s]"
        text = segment.text.strip()
        print(f"{timestamp} {text}")
        full_text.append(text)
    
    # Save to file
    output_file = os.path.splitext(audio_file)[0] + "_transcription.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(" ".join(full_text))
    
    print(f"\n{'-' * 50}")
    print(f"Transcription saved to: {output_file}")
    
    return " ".join(full_text)


def main():
    """Main function with command line interface"""
    
    if len(sys.argv) < 2:
        print("Usage: python transcriber.py <audio_file> [model_size] [device]")
        print("\nModel sizes: tiny, base, small, medium, large-v2, large-v3")
        print("Devices: cpu, cuda, auto")
        print("\nExample:")
        print("  python transcriber.py recording.mp3")
        print("  python transcriber.py recording.mp3 small cuda")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    model_size = sys.argv[2] if len(sys.argv) > 2 else "base"
    device = sys.argv[3] if len(sys.argv) > 3 else "cpu"
    
    transcribe_audio(audio_file, model_size, device)


if __name__ == "__main__":
    main()