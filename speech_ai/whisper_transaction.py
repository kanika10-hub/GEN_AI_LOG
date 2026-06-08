!pip install openai-whisper
!pip install torch

import whisper

model = whisper.load_model("large")

# tiny / base / small / medium / large

# result = model.transcribe(
#     "audio_sample.mp3",
#     fp16=False,
#     verbose=True
# )

# print("\n=== Transcription ===")
# print(result["text"])

# print("\n=== Detected Language ===")
# print(result["language"])



hindi_result = model.transcribe(
    "hindi_speech.mp3",
    language="ta",
    fp16=False,
    verbose=True
)

print("\n=== Hindi Transcription ===")
print(hindi_result["text"])


translated_result = model.transcribe(
    "hindi_speech.mp3",
    task="translate",
    fp16=False,
    verbose=True
)

print("\n=== English Translation ===")
print(translated_result["text"])
