import os

from config import args
from transformers import AutoModel

def check_directory(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")

def set_requires_grad(model, requires_grad):
    for param in model.parameters():
        param.requires_grad = requires_grad
        
def get_feature_extractor():
    feature_extractor = AutoModel.from_pretrained(args.feature_extractor_id)
    return feature_extractor