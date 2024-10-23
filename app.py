import streamlit as st
import numpy as np
import requests
import soundfile as sf

def check_grammar(text):
    url = "https://api.languagetool.org/v2/check"
    params = {
        'text': text,
        'language': 'en-US'
    }
    response = requests.post(url, data=params)
    return response.json().get('matches', [])

def process_input(user_input):
    matches = check_grammar(user_input)
    return matches

# Streamlit title
st.title("IELTS Grammar Checker")

# Audio input
audio_input = st.file_uploader("Upload an audio file", type=["wav"])

if audio_input:
    # Read the audio file
    audio_data, sample_rate = sf.read(audio_input)
    # Placeholder for transcribed text
    user_input = "This is a placeholder for the transcribed text."  # Replace with actual transcription code
else:
    user_input = st.text_area("Type your sentence here:")

if st.button("Check Grammar"):
    matches = process_input(user_input)
    
    if not matches:
        st.success("Great job! Your sentence is perfect!")
    else:
        st.error("There are some errors in your sentence:")
        for match in matches:
            st.write(f"Error: {match['message']}")
            st.write(f"Suggestion: {', '.join([r['value'] for r in match['replacements']])}")
            st.write(f"Context: {match['context']['text']}")
