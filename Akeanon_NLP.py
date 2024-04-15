import streamlit as st
import google.generativeai as genai
import pandas as pd

GOOGLE_API_KEY=st.secrets['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)

def handle_gemini_response(response):
  try:
    # Try using the quick text accessor
    return response.text
  except ValueError as e:
    if "response.text" in str(e) and "no valid Part" in str(e):
      # Access safety ratings for debugging (optional)
      print(f"Error: No valid response part. Safety Ratings: {response.prompt_feedback.safety_ratings}")
      # Handle the error here. You can retry with a different prompt, 
      # return a default value, or raise a new exception.
      raise Exception("No valid response received from Gemini. Consider revising the prompt.")
    else:
      # Raise the original error for unexpected exceptions
      raise e

def app():
    st.title("Akeanon NLP")
    st.write("This app uses Google's Natural Language Processing API to analyze Akeanon text.")

    st.subheader("Akeanon Sentences used for the training")
    df = pd.read_csv('./akeanon-sentences.csv', header=0, index_col=None)
    df = df.reset_index(drop=True)
    st.write(df)
    st.write ("Please use sentences similar to the ones above for better results.")
    model = genai.GenerativeModel(model_name="akeanon-sentences")

    text_input = st.text_area("Enter Akeanon text here:")
    if st.button("Translate to English"):
        try:
            result = model.generate_content(f'translate to English: {text_input}')
            text = handle_gemini_response(result)
            st.write(result.text)
        except Exception as e:
            st.write(f"An error occured: {e}")

    if st.button("Translate to Akeanon"):
        try:
            result = model.generate_content(f'translate to Akeanon: {text_input}')
            text = handle_gemini_response(result)
            st.write(result.text)
        except Exception as e:
            st.write(f"An error occured: {e}")

    st.write("Powered by Google Cloud Natural Language API")


if __name__ == "__main__":
    app()