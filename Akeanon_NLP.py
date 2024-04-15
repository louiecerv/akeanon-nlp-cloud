import streamlit as st
from google_auth_oauthlib import flow

# Define the Google OAuth 2.0 client ID and secret
CLIENT_ID = st.secrets['GOOGLE_CLIENT_ID']
CLIENT_SECRET = st.secrets['GOOGLE_CLIENT_SECRET']
REDIRECT_URI = st.secrets['REDIRECT_URI']

def app():
    # Set up the OAuth 2.0 flow for Google
    myflow = flow.InstalledAppFlow.from_client_secrets_file(
        './security/client_secret.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/generative-language.tuning', 'https://www.googleapis.com/auth/generative-language.retriever'])

    # Authenticate the user
    st.title('Akeanon NLP')

    # Redirect the user to the Google OAuth consent screen to sign in
    auth_url, _ = myflow.authorization_url(prompt='consent')
    st.write('Click below to sign in with Google:')
    st.markdown(f'[Sign in with Google]({auth_url})')


    # After the user signs in, handle the OAuth callback
    if 'code' in st.session_state:
        flow.fetch_token(code=st.session_state.code)
        credentials = flow.credentials
        st.write('Successfully authenticated!')
        st.write('User Information:')
        st.write('Name:', credentials.id_token['name'])
        st.write('Email:', credentials.id_token['email'])
    else:
        st.write('Waiting for authentication...')    

    st.write('Available base models:', [m.name for m in genai.list_models()])

if __name__ == "__main__":
    app()