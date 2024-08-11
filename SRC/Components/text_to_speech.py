from gtts import gTTS

def text_2_speech(text, file_path):
    language = 'en'
    audio_obj = gTTS(text=text, lang=language, slow=False)
    audio_obj.save(file_path)
    return file_path
