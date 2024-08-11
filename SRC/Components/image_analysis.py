import re
from PIL import Image
from nltk.tokenize import sent_tokenize
from SRC.Components.model_pipeline import get_pipeline
from SRC.Components.config import max_tokens

pipe = get_pipeline()

def image_2_text(input_image, input_text):
    image = Image.open(input_image)
    prompt_template = """
    Describe the Image using as much detail as possible.
    Generate a clear and helpful summary or answer related to the image based on your description.
    As you are a Helpful Assistant who is able to answer questions about the image.
    What is the Image all about ?
    Now generate a helpful answer about the image.
    """ + ' '.join(input_text) if type(input_text) == tuple else """
    Act as an expert in imagery descriptive analysis. Using as much detail as possible from the image, respond to the following prompt:
    """ + input_text
    
    prompt = "USER: <image>\n" + prompt_template + "\nASSISTANT:\n"
    response = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": max_tokens})
    
    if response is not None and len(response[0]["generated_text"]) > 0:
        match = re.search(r"ASSISTANT:\s*(.*)", response[0]["generated_text"])
        if match:
            reply = match.group(1).strip()
        else:
            reply = "No Response Found"
    else:
        reply = "No Response Generated"
    
    return reply
