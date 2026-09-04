
import random
import time
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ZeeshanBot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        .main {
            padding-top: 2rem;
        }

        .stChatMessage {
            border-radius: 15px;
        }

        .chat-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 0;
        }

        .chat-subtitle {
            text-align: center;
            color: #777;
            margin-bottom: 30px;
        }

        .footer {
            text-align: center;
            color: #888;
            font-size: 13px;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm **ZeeshanBot**.\n\n"
                "Ask me anything and I'll try my best to help you! 🤖"
            )
        }
    ]


# ============================================================
# BOT RESPONSES
# ============================================================

RESPONSES = {
    "hello": [
        "Hello! 👋 How can I help you today?",
        "Hi there! 😊 What can I do for you?",
        "Hey! 🤖 Nice to meet you!"
    ],

    "hi": [
        "Hi! 👋 How can I help?",
        "Hello! 😊 What would you like to know?"
    ],

    "hey": [
        "Hey! 👋 What's up?",
        "Hello! 🤖 How can I help you?"
    ],

    "how are you": [
        "I'm doing great! 🤖 Thanks for asking!",
        "I'm just a bot, but I'm running perfectly! 😄"
    ],

    "what is your name": [
        "My name is **ZeeshanBot** 🤖.",
        "You can call me **ZeeshanBot**! 🚀"
    ],

    "who are you": [
        "I'm ZeeshanBot, a chatbot built using Python and Streamlit! 🤖"
    ],

    "what can you do": [
        (
            "I can chat with you, answer simple questions, "
            "and respond to different messages. 🚀\n\n"
            "You can make me even smarter by connecting me "
            "to an AI model later!"
        )
    ],

    "thanks": [
        "You're welcome! 😊",
        "No problem! 👍",
        "Anytime! 🤖"
    ],

    "thank you": [
        "You're very welcome! 😊",
        "Happy to help! 🙌"
    ],

    "bye": [
        "Goodbye! 👋 Have a great day!",
        "See you later! 🤖",
        "Bye! Take care! 😊"
    ]
}


# ============================================================
# BOT FUNCTION
# ============================================================

def get_response(user_input):
    """
    Generate a response based on the user's message.
    """

    # Clean the input
    message = user_input.strip().lower()

    # Remove common punctuation
    message = message.replace("?", "")
    message = message.replace("!", "")
    message = message.replace(".", "")

    # Check exact/partial matches
    for keyword, responses in RESPONSES.items():

        if keyword in message:
            return random.choice(responses)

    # Fallback responses
    fallback_responses = [
        "I'm not sure how to answer that yet. 🤔",
        "Interesting question! I don't know the answer to that yet.",
        "I haven't learned how to answer that question. 🧠",
        "Could you rephrase that? I'll try my best! 😊",
        "I'm still learning! Try asking me something else. 🚀"
    ]

    return random.choice(fallback_responses)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.title("🤖 ZeeshanBot")

    st.write(
        "A simple chatbot built with **Python + Streamlit**."
    )

    st.divider()

    st.subheader("💡 Try asking")

    st.write("• Hello")
    st.write("• How are you?")
    st.write("• What is your name?")
    st.write("• What can you do?")
    st.write("• Thank you")
    st.write("• Bye")

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Chat cleared! 🧹\n\n"
                    "Hello again! How can I help you?"
                )
            }
        ]

        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<p class="chat-title">🤖 ZeeshanBot</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="chat-subtitle">Your simple Python-powered chatbot</p>',
    unsafe_allow_html=True
)


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "💬 Type your message here..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if user_input:

    # Save user's message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    response = get_response(user_input)

    # Display assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking... 🤔"):
            time.sleep(0.5)

        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<p class="footer">Made with ❤️ using Python & Streamlit</p>',
    unsafe_allow_html=True
)

