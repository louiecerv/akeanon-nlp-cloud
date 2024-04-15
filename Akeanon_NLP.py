import pprint
import streamlit as st
import google.generativeai as genai
from load_creds import load_creds

def app():
    creds = load_creds()
    genai.configure(credentials=creds)
    st.write('Available base models:', [m.name for m in genai.list_models()])

if __name__ == "__main__":
    app()