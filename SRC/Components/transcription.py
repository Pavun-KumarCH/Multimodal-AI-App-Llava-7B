import whisper
from SRC.Components.utils import writehistory
from SRC.Components.config import Device

model = whisper.load_model("medium", device=Device)

def transcribe(audio):
    if audio is None or audio == "":
        return '', '', None
    
    audio_data = whisper.load_audio(audio)
    audio_data = whisper.pad_or_trim(audio_data)
    mel = whisper.log_mel_spectrogram(audio_data).to(model.device)
    
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    writehistory(f"Detected Language: {detected_language}")
    
    options = whisper.DecodingOptions()
    results = whisper.decode(model, mel, options)
    results_text = results.text
    
    return results_text, detected_language
