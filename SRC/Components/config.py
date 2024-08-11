import torch

max_tokens = 250
Device = "cuda" if torch.cuda.is_available() else "cpu"
