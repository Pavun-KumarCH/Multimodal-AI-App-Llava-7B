import gradio as gr
from SRC.Components.transcription import transcribe
from SRC.Components.image_analysis import image_2_text
from SRC.Components.text_to_speech import text_2_speech
from SRC.Components.config import max_tokens

def process_inputs(audio_path, image_path, confidence_threshold, include_image_analysis, selected_option):
    speech_to_text_output = transcribe(audio_path)
    
    if include_image_analysis and image_path:
        chatgpt_output = image_2_text(image_path, speech_to_text_output)
    else:
        chatgpt_output = "Image analysis not included."
    
    processed_audio_path = text_2_speech(chatgpt_output, "Temp.mp3")
    
    debug_info = {
        "confidence_threshold": confidence_threshold,
        "selected_option": selected_option,
        "include_image_analysis": include_image_analysis
    }
    
    return speech_to_text_output, chatgpt_output, processed_audio_path, None, debug_info

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources="microphone", type="filepath"),
        gr.Image(type="filepath"),
        gr.Slider(minimum=0, maximum=10, value=5, label="Confidence Threshold"),
        gr.Checkbox(label="Include Image Analysis"),
        gr.Dropdown(choices=["Option 1", "Option 2", "Option 3"], label="Select Option")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="AI Response"),
        gr.Audio(label="Generated Audio"),
        gr.Image(label="Image Analysis Result"),
        gr.JSON(label="Debug Info")
    ],
    title="LLM Powered Voice Assistance for Multimodal Data",
    description="Upload your image and interact via voice input and audio responses. Adjust settings and view additional outputs.",
    theme="default",
    live=False
)

iface.launch(debug=True)
