import streamlit as st
import json
from models.chatbot import ChatBot
from utils.config import CHATBOT_NAME, CREATOR_NAME

# Page configuration
st.set_page_config(
    page_title="Family AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background: linear gradient(135deg, #667eea 0%, #764ba2 100%); }
    .stChatMessage { border-radius: 10px; }
    .user-message { background-color: #e1f5ff; }
    .bot-message { background-color: #f3e5f5; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown(f"<h1 style='text-align: center; color: #667eea;'>🤖 {CHATBOT_NAME}</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Your friendly family chatbot assistant</p>", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chatbot = ChatBot()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything...", key="chat_input"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        response = st.session_state.chatbot.get_response(prompt)
        st.markdown(response)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown(f"**Created by:** {CREATOR_NAME}")
    st.markdown("**Version:** 1.0.0")
    st.markdown("[GitHub](https://github.com/deepankur-06/ai)")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
