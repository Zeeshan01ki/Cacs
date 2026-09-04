import streamlit as st
a=st.chat_input("Ask me anything")
if a:
    st.chat_message("user").write(a)
    if a.lower()=="hello":
        st.chat_message("assistant").write("Hello! How can I help you today?")
    elif a.lower()=="how are you?":
        st.chat_message("assistant").write("I'm just a bot, but I'm doing great! How about you?")
    elif a.lower()=="what is your name?":
        st.chat_message("assistant").write("I'm a chatbot created by OpenAI. You can call me ChatGPT!")
    elif a.lower()=="what can you do?":
        st.chat_message("assistant").write("I can answer questions, provide information, and have conversations on a wide range of topics. Feel free to ask me anything!")
    elif a.lower()=="bye":
        st.chat_message("assistant").write("Goodbye! Have a great day!")
    else:
        st.chat_message("assistant").write("I'm sorry, I don't understand that. Can you please rephrase your question or ask something else?")
