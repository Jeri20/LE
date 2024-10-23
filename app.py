import streamlit as st
import torch
from gramformer import Gramformer

# Initialize Gramformer
@st.cache_resource
def load_gramformer():
    gf = Gramformer(models=3, use_gpu=torch.cuda.is_available())
    return gf

# Load the model
gramformer = load_gramformer()

# Streamlit title
st.title("Enhanced English Grammar Checker with Gramformer")

# User input
user_input = st.text_area("Type your sentence here:")

if st.button("Check Grammar"):
    if user_input:
        # Run correction
        corrected_sentence = gramformer.correct(user_input)[0]
        st.write("Corrected Sentence:", corrected_sentence)
    else:
        st.warning("Please enter a sentence to check.")
