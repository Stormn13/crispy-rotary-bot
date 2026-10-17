import streamlit as st

with st.chat_message('user'):
    st.text('hi')

with st.chat_message('assistant'):
    st.text('how are you?')

user_input = st.chat_input('type here')