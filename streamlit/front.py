import streamlit as st
import requests

# Title of the app
st.title("Sentiment Analysis Chatbot")

# Local API endpoint
API_URL = "http://localhost:3000/analyze-sentiment" 

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input from user
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send user message to the local API for sentiment analysis
    try:
        response = requests.post(
            API_URL,
            json={"text": prompt},  
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()  # Raise an error for bad status codes
        sentiment_result = response.json().get("sentiment") 
        bot_response = f"Sentiment: {sentiment_result}"
    except Exception as e:
        bot_response = f"Error: {str(e)}"

    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)