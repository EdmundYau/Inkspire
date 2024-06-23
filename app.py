# import streamlit as st
# from audio_recorder_streamlit import audio_recorder
# import openai
# import base64

# def setup_openai_client(api_key):
#     return openai.OpenAI(api_key=api_key)

# def transcribe_audio(client, audio_path):
#     with open(audio_path, "rb") as audio_file:
#         transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
#         return transcript.text

# def fetch_ai_response(client, input_text):
#     messages = [{"role": "user", "content": input_text}]
#     response = client.chat.completions.create(model="gpt-3.5-turbo-1106", messages=messages)
#     return response.choices[0].message.content

# def text_to_audio(client, text, audio_path):
#     response = client.audio.speech.create(model="tts-1", voice="echo", input=text)
#     response.stream_to_file(audio_path)

# def main():
#     st.title("Inkspire")
#     st.write("Welcome to Inkspire! Let's get started.")

#     # Create two columns for the audio recorder and the text area
#     col1, col2 = st.columns([1, 5])  # Adjust the ratio based on your needs

#     with col1:
#         # Place the audio recorder in the first column
#         recorded_audio = audio_recorder(text="Inkspire")
#         if recorded_audio:
#             audio_file = "audio.mp3"
#             with open(audio_file, "wb") as file:
#                 file.write(recorded_audio)

#     with col2:
#         # Place the text area in the second column
#         st.markdown("""
#     <style>
#     .stTextArea [data-baseweb=base-input] {
#         background-image: linear-gradient(140deg, rgb(54, 36, 31) 0%, rgb(121, 56, 100) 50%, rgb(106, 117, 25) 75%);
#         -webkit-text-fill-color: white;
#     }

#     .stTextArea [data-baseweb=base-input] [disabled=""]{
#         background-image: linear-gradient(45deg, red, purple, red);
#         -webkit-text-fill-color: gray;
#     }
#     </style>
#     """,unsafe_allow_html=True)

#         user_input = st.text_area("Press cmd + enter to save...", height=1100)  # Adjust height as needed

#     # API Key Configuration and Processing
#     api_key = "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"
#     if api_key and recorded_audio:
#         client = setup_openai_client(api_key)

#         transcribe_text = transcribe_audio(client, audio_file)
#         st.write("Transcription: ", transcribe_text)

#         preparedText = ("You are an AI English assistant designed to help the user write essays. This includes giving "
#                         "ideas to the user, helping the user think of ideas of what to continue to write about, and "
#                         "overall grammar and structure of MLA essays. Based on the following, respond in one sentence "
#                         "like you are a human speaking to me: ")
#         ai_response = fetch_ai_response(client, preparedText + user_input + transcribe_text)

#         response_audio_file = "response_audio.mp3"
#         text_to_audio(client, ai_response, response_audio_file)
#         st.audio(response_audio_file)
#         st.write("AI Response: ", ai_response)

# if __name__ == '__main__':
#     main()


import streamlit as st
from audio_recorder_streamlit import audio_recorder
import openai
import base64

def setup_openai_client(api_key):
    return openai.OpenAI(api_key=api_key)

def transcribe_audio(client, audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
        return transcript.text

def fetch_ai_response(client, input_text):
    messages = [{"role": "user", "content": input_text}]
    response = client.chat.completions.create(model="gpt-4-turbo", messages=messages)
    return response.choices[0].message.content

def text_to_audio(client, text, audio_path):
    response = client.audio.speech.create(model="tts-1", voice="nova", input=text)
    response.stream_to_file(audio_path)

def main():
    st.set_page_config(layout="wide", page_title="Inkspire")
    st.title("Inkspire")
    st.write("Welcome to Inkspire! Let's get started.")
    

    # Create two columns for the audio recorder and the text area
    col1, spacer, col2 = st.columns([10, 0.5, 5])  # Adjusted ratios to give more width to col1 and col2

    with col2:
            # Place the audio recorder in the first column
            recorded_audio = audio_recorder(text="")
            if recorded_audio:
                audio_file = "audio.mp3"
                with open(audio_file, "wb") as file:
                    file.write(recorded_audio)

    with spacer:
        st.write("")  # This spacer column will be empty

    with col1:
        # Place the text area in the second column
        st.markdown("""
            <style>
            .stTextArea [data-baseweb=base-input] {
                background-image: linear-gradient(140deg, rgb(54, 36, 31) 0%, rgb(121, 56, 100) 50%, rgb(106, 117, 25) 75%);
                -webkit-text-fill-color: white;
            }

            .stTextArea [data-baseweb=base-input] [disabled=""]{
                background-image: linear-gradient(45deg, red, purple, red);
                -webkit-text-fill-color: gray;
            }
            </style>
            """,unsafe_allow_html=True)

        user_input = st.text_area("Press cmd + enter to save...", height=1100)  # Adjust height as needed

    with col2:
        # API Key Configuration and Processing
        api_key = "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"
        if api_key and recorded_audio:
            client = setup_openai_client(api_key)

            transcribe_text = transcribe_audio(client, audio_file)
            st.write("Transcription: ", transcribe_text)

            preparedText = ("You are an AI English assistant designed to help the user write essays. This includes giving "
                            "ideas to the user, helping the user think of ideas of what to continue to write about, and "
                            "overall grammar and structure of MLA essays. Based on the following, respond in one sentence "
                            "like you are a human speaking to me: ")
            ai_response = fetch_ai_response(client, preparedText + user_input + transcribe_text)

            response_audio_file = "response_audio.mp3"
            text_to_audio(client, ai_response, response_audio_file)
            st.audio(response_audio_file)
            st.write("Inkspired's Response: ", ai_response)

if __name__ == '__main__':
    main()
