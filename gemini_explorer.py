import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "sample-gemini"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.5,
)

# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)

chat = model.start_chat()
