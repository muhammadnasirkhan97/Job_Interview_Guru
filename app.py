# => 03 using only text base question
import streamlit as st
from transformers import pipeline
from gtts import gTTS
from io import BytesIO
import re
import torch

# Set device for optimal performance
device = 0 if torch.cuda.is_available() else -1

# Load the question-answering pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", device=device)

st.title("Interview Preparation Chatbot")
st.write("Ask interview questions about programming concepts through text.")

# Context for the question-answering model
context = """
Python lists are collections of data stored in a single variable. They are ordered, mutable, and allow duplicate values. 
Lists are created with square brackets []. Here are some list operations: append(), remove(), len(), and slicing.
"""

# Function to clean input text for better model responses
def clean_input(input_text):
    # Remove extra characters like punctuation
    input_text = re.sub(r'[^a-zA-Z0-9\s]', '', input_text)
    return input_text

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text)
    audio_output = BytesIO()
    tts.write_to_fp(audio_output)
    st.audio(audio_output, format="audio/mp3")

# User input for text
user_question = st.text_input("Type your question here:")

# Check if question exists and process it
if user_question:
    # Clean and prepare the question
    cleaned_question = clean_input(user_question)
    st.write(f"**Cleaned Question:** {cleaned_question}")

    # Generate response based on the question
    response = qa_pipeline(question=cleaned_question, context=context)
    answer_text = response['answer']
    st.write(f"**Answer:** {answer_text}")

    # Option to play answer in voice
    if st.button("Play Answer"):
        text_to_speech(answer_text)


# # => 02 updated code 
# import streamlit as st
# from transformers import pipeline
# import speech_recognition as sr
# from gtts import gTTS
# from io import BytesIO
# import re
# import torch

# # Set device for optimal performance
# device = 0 if torch.cuda.is_available() else -1

# # Load the question-answering pipeline
# qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", device=device)

# st.title("Interview Preparation Chatbot")
# st.write("Ask interview questions about programming concepts through text or voice.")

# # Context for the question-answering model
# context = """
# Python lists are collections of data stored in a single variable. They are ordered, mutable, and allow duplicate values. 
# Lists are created with square brackets []. Here are some list operations: append(), remove(), len(), and slicing.
# """

# # Function to clean input text for better model responses
# def clean_input(input_text):
#     # Remove extra characters like punctuation
#     input_text = re.sub(r'[^a-zA-Z0-9\s]', '', input_text)
#     return input_text

# # Function to capture voice input
# def get_voice_input():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             question = recognizer.recognize_google(audio)
#             st.write(f"You asked: {question}")
#             return question
#         except sr.UnknownValueError:
#             st.write("Could not understand the audio.")
#         except sr.RequestError:
#             st.write("Voice recognition service is unavailable.")
#     return None

# # Function to convert text to speech
# def text_to_speech(text):
#     tts = gTTS(text)
#     audio_output = BytesIO()
#     tts.write_to_fp(audio_output)
#     st.audio(audio_output, format="audio/mp3")

# # User input options for text or voice
# st.write("Choose to either type or speak your question.")
# user_question = st.text_input("Type your question here:")

# if st.button("Record Question"):
#     user_question = get_voice_input()

# # Check if question exists and process it
# if user_question:
#     # Clean and prepare the question
#     cleaned_question = clean_input(user_question)
#     st.write(f"**Cleaned Question:** {cleaned_question}")

#     # Generate response based on the question
#     response = qa_pipeline(question=cleaned_question, context=context)
#     answer_text = response['answer']
#     st.write(f"**Answer:** {answer_text}")

#     # Option to play answer in voice
#     if st.button("Play Answer"):
#         text_to_speech(answer_text)


# # => 01 real time voice 
# import streamlit as st
# from transformers import pipeline
# import speech_recognition as sr
# from gtts import gTTS
# from io import BytesIO
# import torch

# # Check if GPU is available
# device = 0 if torch.cuda.is_available() else -1

# # Load the Hugging Face model on the correct device
# qa_pipeline = pipeline("text-generation", model="gpt2", device=device)

# st.title("Interview Preparation Chatbot")
# st.write("Speak your interview questions directly into the microphone.")

# # Function to capture real-time audio from the microphone
# def get_voice_input():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             question = recognizer.recognize_google(audio)
#             st.write(f"You asked: {question}")
#             return question
#         except sr.UnknownValueError:
#             st.write("Could not understand the audio.")
#         except sr.RequestError:
#             st.write("Voice recognition service is unavailable.")
#     return None

# # Text-to-speech function to convert answer to speech
# def text_to_speech(text):
#     tts = gTTS(text)
#     audio_output = BytesIO()
#     tts.write_to_fp(audio_output)
#     st.audio(audio_output, format="audio/mp3")

# # Real-time voice input button
# if st.button("Record Question"):
#     question = get_voice_input()

#     if question:
#         # Generate response based on the question
#         response = qa_pipeline(question, max_length=50, do_sample=True, truncation=True)
#         answer_text = response[0]['generated_text']
#         st.write(f"**Answer:** {answer_text}")

#         # Play the answer as audio
#         if st.button("Play Answer"):
#             text_to_speech(answer_text)


# # => 00 recorder voice
# import streamlit as st
# from transformers import pipeline
# import speech_recognition as sr
# from gtts import gTTS
# from io import BytesIO
# import torch

# # Check if GPU is available
# device = 0 if torch.cuda.is_available() else -1

# # Load the Hugging Face model on the correct device
# qa_pipeline = pipeline("text-generation", model="gpt2", device=device)

# st.title("Interview Preparation Chatbot")
# st.write("Ask your interview questions by typing or uploading an audio file.")

# # Function to capture audio from an uploaded file
# def get_voice_input():
#     uploaded_file = st.file_uploader("Upload an audio file (.wav) containing your question", type=["wav"])
#     if uploaded_file is not None:
#         recognizer = sr.Recognizer()
#         with sr.AudioFile(uploaded_file) as source:
#             audio = recognizer.record(source)
#         try:
#             question = recognizer.recognize_google(audio)
#             st.write(f"You asked: {question}")
#             return question
#         except sr.UnknownValueError:
#             st.write("Could not understand the audio.")
#         except sr.RequestError:
#             st.write("Voice recognition service is unavailable.")
#     return None

# # Text-to-speech function
# def text_to_speech(text):
#     tts = gTTS(text)
#     audio_output = BytesIO()
#     tts.write_to_fp(audio_output)
#     st.audio(audio_output, format="audio/mp3")

# # Input selection
# input_type = st.radio("Choose input method:", ("Text", "Voice"))

# question = None
# if input_type == "Text":
#     question = st.text_input("Type your question:")
# elif input_type == "Voice":
#     question = get_voice_input()

# # Generate answer if question is available
# if st.button("Get Answer") and question:
#     response = qa_pipeline(question, max_length=50, do_sample=True, truncation=True)
#     answer_text = response[0]['generated_text']
#     st.write(f"**Answer:** {answer_text}")
    
#     # Optionally play the answer as audio
#     if st.button("Play Answer"):
#         text_to_speech(answer_text)
