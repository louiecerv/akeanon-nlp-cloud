import base64
import google.generativeai as genai
import streamlit as st
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
from load_creds import load_creds

creds = load_creds()

genai.configure(credentials=creds)

def app():
    st.title("Akeanon NLP")
    st.write("This app uses Google's Natural Language Processing API to analyze Akeanon text.")

    st.write('Available base models:', [m.name for m in genai.list_models()])

#run the app
if __name__ == "__main__":
  app()
