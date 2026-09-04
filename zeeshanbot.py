
import random
import time
from datetime import datetime

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EventBooker",
    page_icon="🎟️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
        padding-bottom: 5rem;
    }

    .hero {
        text-align: center;
        padding: 25px 10px;
    }

    .hero h1 {
        font-size: 3.2rem;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 1.1rem;
        opacity: 0.65;
    }

    .event-card {
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 15px;
    }

    .event-title {
        font-size: 1.4rem;
        font-weight: 700;
    }

    .event-info {
        opacity: 0.75;
        margin-top: 5px;
    }

    .footer {
        text-align: center;
        opacity: 0.5;
        font-size: 0.8rem;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# EVENT DATABASE
# ============================================================

EVENTS = [
    {
        "id": 1,
        "name": "Tech Innovation Summit 2026",
        "category": "Technology",
        "date": "October 10, 2026",
        "time": "10:00 AM",
        "location": "Mumbai Convention Centre",
        "price": 999,
        "available": 120,
        "description": (
            "A technology conference featuring AI, robotics, "
            "cloud computing, startups and future technology."
        ),
    },
    {
        "id": 2,
        "name": "Mumbai Music Festival",
        "category": "Music",
        "date": "October 18, 2026",
        "time": "6:00 PM",
        "location": "Jio World Garden, Mumbai",
        "price": 1499,
        "available": 250,
        "description": (
            "Enjoy an unforgettable evening of live music, "
            "performances and entertainment."
        ),
    },
    {
        "id": 3,
        "name": "Startup & Business Expo",
        "category": "Business",
        "date": "November 2, 2026",
        "time": "9:30 AM",
        "location": "Bandra Exhibition Centre",
        "price": 799,
        "available": 180,
        "description": (
            "Meet entrepreneurs, investors and business leaders "
            "and discover new startup opportunities."
        ),
    },
    {
        "id": 4,
        "name": "Food & Culture Festival",
        "category": "Food",
        "date": "November 15, 2026",
        "time": "12:00 PM",
        "location": "Nesco Grounds, Mumbai",
        "price": 499,
        "available": 500,
        "description": (
            "Explore delicious food, local culture, live cooking "
            "and entertainment from across India."
        ),
    },
    {
        "id": 5,
        "name": "Photography Workshop",
        "category": "Workshop",
        "date": "December 5, 2026",
        "time": "11:00 AM",
        "location": "Kala Ghoda, Mumbai",
        "price": 599,
        "available": 35,
        "description": (
            "A hands-on photography workshop for beginners "
            "and photography enthusiasts."
        ),
    },
]


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Welcome to **EventBooker**!\n\n"
                "I can help you find events, check ticket prices, "
                "and guide you through booking tickets. 🎟️\n\n"
                "Try asking:\n"
                "- What events are available?\n"
                "- Show me technology events\n"
                "- How much is the music festival?\n"
                "- I want to book tickets"
            ),
            "time": datetime.now().strftime("%I:%M %p"),
        }
    ]


if "bookings" not in st.session_state:
    st.session_state.bookings = []


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_time():
    return datetime.now().strftime("%I:%M %p")


def find_event(event_name):
    """Find an event using a partial name."""

    event_name = event_name.lower()

    for event in EVENTS:
        if (
            event_name in event["name"].lower()
            or event["name"].lower() in event_name
        ):
            return event

    return None


def event_list_text(events):
    """Create a readable event list."""

    if not events:
        return "I couldn't find any matching events. 😕"

    result = "### 🎟️ Available Events\n\n"

    for event in events:
        result += (
            f"**{event['name']}**\n"
            f"📅 {event['date']} • ⏰ {event['time']}\n"
            f"📍 {event['location']}\n"
            f"💰 ₹{event['price']} per ticket\n"
            f"🎫 {event['available']} tickets available\n\n"
        )

    return result


# ============================================================
# CHATBOT RESPONSE ENGINE
# ============================================================

def get_response(user_input):
    """Generate a response based on the user's message."""

    message = user_input.lower().strip()

    # --------------------------------------------------------
    # Greeting
    # --------------------------------------------------------

    if any(word in message for word in ["hello", "hi", "hey"]):
        return (
            "Hello! 👋 Welcome to **EventBooker**!\n\n"
            "How can I help you with your event booking today?"
        )

    # --------------------------------------------------------
    # Show all events
    # --------------------------------------------------------

    if (
        "available events" in message
        or "all events" in message
        or "show events" in message
        or message == "events"
        or "what events" in message
    ):
        return event_list_text(EVENTS)

    # --------------------------------------------------------
    # Technology
    # --------------------------------------------------------

    if (
        "technology" in message
        or "tech event" in message
        or "tech events" in message
    ):
        events = [
            event
            for event in EVENTS
            if event["category"] == "Technology"
        ]

        return event_list_text(events)

    # --------------------------------------------------------
    # Music
    # --------------------------------------------------------

    if "music" in message:
        events = [
            event
            for event in EVENTS
            if event["category"] == "Music"
        ]

        return event_list_text(events)

    # --------------------------------------------------------
    # Business
    # --------------------------------------------------------

    if (
        "business" in message
        or "startup" in message
    ):
        events = [
            event
            for event in EVENTS
            if event["category"] == "Business"
        ]

        return event_list_text(events)

    # --------------------------------------------------------
    # Food
    # --------------------------------------------------------

    if "food" in message:
        events = [
            event
            for event in EVENTS
            if event["category"] == "Food"
        ]

        return event_list_text(events)

    # --------------------------------------------------------
    # Workshop
    # --------------------------------------------------------

    if "workshop" in message:
        events = [
            event
            for event in EVENTS
            if event["category"] == "Workshop"
        ]

        return event_list_text(events)

    # --------------------------------------------------------
    # Price questions
    # --------------------------------------------------------

    if (
        "price" in message
        or "cost" in message
        or "ticket price" in message
        or "how much" in message
    ):

        if "music" in message:
            event = find_event("Mumbai Music Festival")

        elif "technology" in message or "tech" in message:
            event = find_event("Tech Innovation Summit")

        elif "business" in message or "startup" in message:
            event = find_event("Startup Business")

        elif "food" in message:
            event = find_event("Food Culture")

        elif "photography" in message:
            event = find_event("Photography")

        else:
            return (
                "Sure! 💰 Which event would you like the price for?\n\n"
                "For example: **What is the price of the music festival?**"
            )

        if event:
            return (
                f"🎟️ **{event['name']}**\n\n"
                f"Ticket price: **₹{event['price']}** per person."
            )

    # --------------------------------------------------------
    # Location questions
    # --------------------------------------------------------

    if (
        "where" in message
        or "location" in message
        or "venue" in message
    ):

        if "music" in message:
            event = find_event("Mumbai Music Festival")

        elif "technology" in message or "tech" in message:
            event = find_event("Tech Innovation Summit")

        elif "food" in message:
            event = find_event("Food Culture")

        elif "photography" in message:
            event = find_event("Photography")

        else:
            return (
                "Which event are you looking for? 📍\n\n"
                "Tell me the event name and I'll show you its venue."
            )

        if event:
            return (
                f"📍 **{event['name']}** is being held at:\n\n"
                f"**{event['location']}**"
            )

    # --------------------------------------------------------
    # Booking
    # --------------------------------------------------------

    if any(
        word in message
        for word in [
            "book",
            "booking",
            "reserve",
            "reservation",
            "ticket",
            "tickets",
        ]
    ):

        return (
            "🎟️ I'd be happy to help you book tickets!\n\n"
            "Please select an event from the **Book Tickets** "
            "section in the sidebar.\n\n"
            "You can choose the event and number of tickets there."
        )

    # --------------------------------------------------------
    # Cancellation
    # --------------------------------------------------------

    if (
        "cancel" in message
        or "cancellation" in message
    ):
        return (
            "❌ For cancellation requests, please provide your "
            "booking ID.\n\n"
            "You can also check your bookings in the sidebar."
        )

    # --------------------------------------------------------
    # My bookings
    # --------------------------------------------------------

    if (
        "my booking" in message
        or "my bookings" in message
        or "bookings" in message
    ):

        if not st.session_state.bookings:
            return "You don't have any bookings yet. 🎟️"

        result = "### 🎫 Your Bookings\n\n"

        for booking in st.session_state.bookings:
            result += (
                f"**Booking ID:** {booking['id']}\n"
                f"Event: {booking['event']}\n"
                f"Tickets: {booking['tickets']}\n"
                f"Total: ₹{booking['total']}\n\n"
            )

        return result

    # --------------------------------------------------------
    # Help
    # --------------------------------------------------------

    if "help" in message:
        return (
            "### 🤖 What I can do\n\n"
            "🎟️ Find events\n\n"
            "💰 Check ticket prices\n\n"
            "📍 Show event locations\n\n"
            "🎫 Help you book tickets\n\n"
            "📋 Show your bookings\n\n"
            "❌ Explain cancellation options"
        )

    # --------------------------------------------------------
    # Thanks
    # --------------------------------------------------------

    if (
        "thanks" in message
        or "thank you" in message
    ):
        return (
            "You're very welcome! 😊\n\n"
            "Enjoy your event! 🎉"
        )

    # --------------------------------------------------------
    # Goodbye
    # --------------------------------------------------------

    if (
        message == "bye"
        or "goodbye" in message
    ):
        return (
            "Goodbye! 👋\n\n"
            "Hope to see you at an amazing event soon! 🎉"
        )

    # --------------------------------------------------------
    # Fallback
    # --------------------------------------------------------

    return (
        "I'm not sure I understood that. 🤔\n\n"
        "I can help you with:\n"
        "🎟️ Finding events\n"
        "💰 Ticket prices\n"
        "📍 Event locations\n"
        "🎫 Booking tickets\n"
        "📋 Your bookings\n\n"
        "Try asking **'What events are available?'**"
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎟️ EventBooker")

    st.caption(
        "Find and book amazing events."
    )

    st.divider()

    # --------------------------------------------------------
    # Book Tickets
    # --------------------------------------------------------

    st.subheader("🎫 Book Tickets")

    event_names = [
        event["name"]
        for event in EVENTS
        if event["available"] > 0
    ]

    selected_event_name = st.selectbox(
        "Choose an event",
        event_names,
    )

    selected_event = find_event(
        selected_event_name
    )

    ticket_count = st.number_input(
        "Number of tickets",
        min_value=1,
        max_value=10,
        value=1,
    )

    if selected_event:

        total_price = (
            selected_event["price"]
            * ticket_count
        )

        st.info(
            f"💰 Total: ₹{total_price}"
        )

        if st.button(
            "🎟️ Book Now",
            use_container_width=True,
        ):

            if (
                ticket_count
                <= selected_event["available"]
            ):

                booking_id = (
                    f"EB{random.randint(10000, 99999)}"
                )

                booking = {
                    "id": booking_id,
                    "event": selected_event["name"],
                    "tickets": ticket_count,
                    "total": total_price,
                }

                st.session_state.bookings.append(
                    booking
                )

                selected_event["available"] -= (
                    ticket_count
                )

                st.success(
                    f"Booking confirmed! 🎉\n\n"
                    f"Booking ID: **{booking_id}**"
                )

            else:

                st.error(
                    "Not enough tickets available."
                )

    st.divider()

    # --------------------------------------------------------
    # Event categories
    # --------------------------------------------------------

    st.subheader("📂 Categories")

    st.write("💻 Technology")
    st.write("🎵 Music")
    st.write("💼 Business")
    st.write("🍔 Food")
    st.write("📸 Workshop")

    st.divider()

    # --------------------------------------------------------
    # My bookings
    # --------------------------------------------------------

    st.subheader("📋 My Bookings")

    if not st.session_state.bookings:

        st.caption(
            "No bookings yet."
        )

    else:

        for booking in st.session_state.bookings:

            st.write(
                f"🎫 **{booking['id']}**"
            )

            st.caption(
                f"{booking['event']} • "
                f"{booking['tickets']} ticket(s) • "
                f"₹{booking['total']}"
            )

    st.divider()

    # --------------------------------------------------------
    # Clear chat
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">

        <h1>🎟️ EventBooker</h1>

        <p>
            Discover events, check tickets and book your next
            experience.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# EVENT CARDS
# ============================================================

st.subheader("🔥 Featured Events")

columns = st.columns(3)

for index, event in enumerate(EVENTS[:3]):

    with columns[index]:

        st.markdown(
            f"""
            <div class="event-card">

                <div class="event-title">
                    {event['name']}
                </div>

                <div class="event-info">
                    📅 {event['date']}<br>
                    ⏰ {event['time']}<br>
                    📍 {event['location']}<br>
                    💰 ₹{event['price']}<br>
                    🎫 {event['available']} tickets left
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


st.divider()


# ============================================================
# CHAT
# ============================================================

st.subheader("🤖 Event Assistant")


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if "time" in message:
            st.caption(
                message["time"]
            )


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "💬 Ask about events or tickets..."
)


# ============================================================
# PROCESS CHAT
# ============================================================

if user_input:

    # User message
    user_message = {
        "role": "user",
        "content": user_input,
        "time": get_time(),
    }

    st.session_state.messages.append(
        user_message
    )

    with st.chat_message("user"):

        st.markdown(
            user_input
        )

        st.caption(
            user_message["time"]
        )

    # Bot response
    response = get_response(
        user_input
    )

    assistant_message = {
        "role": "assistant",
        "content": response,
        "time": get_time(),
    }

    with st.chat_message("assistant"):

        with st.spinner(
            "Checking events... 🔎"
        ):
            time.sleep(0.5)

        st.markdown(
            response
        )

        st.caption(
            assistant_message["time"]
        )

    st.session_state.messages.append(
        assistant_message
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        🎟️ EventBooker<br>
        Built with ❤️ using Python & Streamlit

    </div>
    """,
    unsafe_allow_html=True,
)
