import streamlit as st
import requests
import soundfile as sf
from textblob import TextBlob

def check_grammar(text):
    url = "https://api.languagetool.org/v2/check"
    params = {
        'text': text,
        'language': 'en-US'
    }
    response = requests.post(url, data=params)
    return response.json().get('matches', [])

def correct_sentence(text, matches):
    corrected_text = text
    for match in matches:
        if match['replacements']:
            suggestion = match['replacements'][0]['value']
            start = match['offset']
            end = match['offset'] + match['length']
            corrected_text = corrected_text[:start] + suggestion + corrected_text[end:]
    return corrected_text

def style_suggestion(text):
    blob = TextBlob(text)
    # Example: return a more formal version of the text
    # You can implement more advanced logic based on TextBlob's functionality
    return str(blob.correct())

# Streamlit title
st.title("Enhanced IELTS Grammar Checker")

# Audio input
audio_input = st.file_uploader("Upload an audio file", type=["wav"])

if audio_input:
    audio_data, sample_rate = sf.read(audio_input)
    user_input = "This is a placeholder for the transcribed text."  # Replace with actual transcription code
else:
    user_input = st.text_area("Type your sentence here:")

if st.button("Check Grammar"):
    matches = check_grammar(user_input)
    
    if not matches:
        st.success("Great job! Your sentence is perfect!")
    else:
        st.error("There are some errors in your sentence:")
        corrected_text = correct_sentence(user_input, matches)
        st.write("Corrected Sentence:", corrected_text)

        # Provide style suggestions
        improved_text = style_suggestion(corrected_text)
        st.write("Improved Sentence:", improved_text)
