import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY=st.secrets['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)
     
def app():
    st.write('Available base models:', [m.name for m in genai.list_models()])

    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content("Please give me python code to sort a list.")
    st.write(response.text)


if __name__ == "__main__":
    app()