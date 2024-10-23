import streamlit as st
import numpy as np
import language_tool_python
import soundfile as sf

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return matches

# Streamlit title
st.title("IELTS Grammar Checker")

# Audio input
audio_input = st.file_uploader("Upload an audio file", type=["wav"])

if audio_input:
    # Read the audio file and process it
    audio_data, sample_rate = sf.read(audio_input)
    # Here you would typically convert audio to text using a speech recognition library
    # For demonstration, we are using a placeholder for the text
    user_input = "This is a placeholder for the transcribed text."
    
    # Replace with actual transcription code
else:
    user_input = st.text_area("Type your sentence here:")

if st.button("Check Grammar"):
    matches = check_grammar(user_input)
    
    if not matches:
        st.success("Great job! Your sentence is perfect!")
    else:
        st.error("There are some errors in your sentence:")
        for match in matches:
            st.write(f"Error: {match.message}")
            st.write(f"Suggestion: {', '.join(match.replacements)}")
            st.write(f"Context: {match.context}")
