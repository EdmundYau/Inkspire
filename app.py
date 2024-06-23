import streamlit as st
from audio_recorder_streamlit import audio_recorder
import openai
import base64
import tkinter as tk


def setup_openai_client(api_key):
      return openai.OpenAI(api_key = api_key)



def transcribe_audio(client, audio_path):
      with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
            return transcript.text
      

def fetch_ai_response(client, input_text):
      messages = [{"role": "user", "content": input_text}]
      response = client.chat.completions.create(model="gpt-3.5-turbo-1106", messages=messages)
      return response.choices[0].message.content


def text_to_audio(client, text, audio_path):
      response = client.audio.speech.create(model="tts-1", voice = "echo", input = text)
      response.stream_to_file(audio_path)

def create_text_card(text, title="Response"):
        return

def main():
    #st.sidebar.title("API KEY CONFIGURATION")
    api_key = "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"
    
    st.title(" Inkspire")
    st.write("Welcome to Inkspire!")
    user_input = st.text_area("Press cmd + enter to save...", height = 800)
    print(user_input)
    print(api_key)
    if api_key:
        #print("check")
        client = setup_openai_client(api_key)
        recorded_audio = audio_recorder(text = "Inkspire")
        #print(recorded_audio) #none


        if recorded_audio:
              print("check")
              audio_file = "audio.mp3"
              with open(audio_file, "wb") as file:
                    file.write(recorded_audio)


                    transcribe_text = transcribe_audio(client, audio_file)
                    st.write("Transcription: ", transcribe_text)
                    preparedText = "You are an AI English assistant that is designed to help the user write essays. This includes giving ideas to the user, helping the user think of ideas of what to continue to write about, and overall grammar and structure of MLA essays. Based on the following, respond in one sentence like you are a human speaking to me: "
                    ai_response = fetch_ai_response(client, preparedText + user_input + transcribe_text)
                    response_audio_file = "response_audio.mp3"
                    text_to_audio(client, ai_response, response_audio_file)
                    st.audio(response_audio_file)
                    st.write("AI Response: ", ai_response)



if __name__ == '__main__':
        main()