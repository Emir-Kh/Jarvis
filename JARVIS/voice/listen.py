from faster_whisper import WhisperModel
from voice.recorder import record_audio

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def listen():
    record_audio()

    segments, info = model.transcribe("voice.wav")

    text = ""

    for segment in segments:
        text += segment.text

    print("You:", text)

    return text.strip()