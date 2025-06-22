import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# File path to your audio file
audio_file_path = "D:\smartbridge_project\part-2\AI in Salesforce： A 2024 Perspective [Sd-41Pgg_w8].mp3"

# Open the audio file in binary mode
with open(audio_file_path, "rb") as audio_file:
    print("Transcribing...")
    transcript = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        response_format="text"  # Use "json" if you need detailed segments
    )

# Save to a .txt file
output_path = "smartbridge_salesforce_ai_transcript.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(transcript)

print(f"Transcription saved to: {output_path}")
