import streamlit as st
from listt import message_history

for message in message_history:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('type here')

if user_input:
    message_history.append({'role' :'user' , 'content' : user_input})
    with st.chat_message('user'):
        st.text(user_input)
    message_history.append({'role' :'assistant' , 'content' : user_input})    
    with st.chat_message('assistant'):
        st.text(user_input)