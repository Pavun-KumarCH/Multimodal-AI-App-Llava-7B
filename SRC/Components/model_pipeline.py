import torch
from transformers import BitsAndBytesConfig, pipeline

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

MODEL_ID = "llava-hf/llava-1.5-7b-hf"
pipe = pipeline("image-to-text",
                model=MODEL_ID,
                model_kwargs={"quantization_config": quantization_config})

def get_pipeline():
    return pipe