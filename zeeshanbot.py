```python
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 My Chatbot")
st.caption("Ask me something and I'll do my best to help!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("💬 Ask me anything...")

if user_input:
    # Show and save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Normalize input
    question = user_input.strip().lower()

    # Chatbot responses
    responses = {
        "hello": "Hello! 👋 How can I help you today?",
        "hi": "Hi there! 😊 What can I do for you?",
        "how are you?": "I'm doing great! 🤖 Thanks for asking. How about you?",
        "what is your name?": "I'm a chatbot created with Streamlit. You can call me ChatBot! 🤖",
        "what can you do?": (
            "I can answer questions, have conversations, "
            "provide information, and much more! 🚀"
        ),
        "bye": "Goodbye! 👋 Have a great day!",
        "thanks": "You're welcome! 😊",
        "thank you": "You're very welcome! 🙌"
    }

    # Find response
    response = responses.get(
        question,
        "I'm not sure how to answer that yet. 🤔 "
        "Try asking me something else!"
    )

    # Display and save assistant response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
```
