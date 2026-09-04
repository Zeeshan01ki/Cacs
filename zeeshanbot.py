
import random
import time
from datetime import datetime

import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EventHub | Event Booking",
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

    /* ---------- GLOBAL ---------- */

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 5rem;
        max-width: 1400px;
    }

    /* ---------- HERO ---------- */

    .hero {
        padding: 35px 25px;
        border-radius: 25px;
        margin-bottom: 30px;
        border: 1px solid rgba(128,128,128,0.18);
        text-align: center;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0;
    }

    .hero-text {
        font-size: 1.15rem;
        opacity: 0.65;
        margin-top: 10px;
    }

    /* ---------- EVENT CARD ---------- */

    .event-card {
        border: 1px solid rgba(128,128,128,0.22);
        border-radius: 20px;
        padding: 22px;
        min-height: 245px;
        margin-bottom: 10px;
    }

    .event-category {
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        opacity: 0.6;
        letter-spacing: 1px;
    }

    .event-name {
        font-size: 1.35rem;
        font-weight: 750;
        margin: 8px 0 14px 0;
    }

    .event-detail {
        font-size: 0.92rem;
        margin: 7px 0;
        opacity: 0.8;
    }

    .event-price {
        font-size: 1.2rem;
        font-weight: 750;
        margin-top: 15px;
    }

    /* ---------- STAT CARD ---------- */

    .stat-card {
        border: 1px solid rgba(128,128,128,0.2);
        border-radius: 16px;
        padding: 18px;
        text-align: center;
    }

    .stat-number {
        font-size: 1.8rem;
        font-weight: 800;
    }

    .stat-label {
        opacity: 0.6;
        font-size: 0.85rem;
    }

    /* ---------- BOOKING CARD ---------- */

    .booking-card {
        border: 1px solid rgba(128,128,128,0.2);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 12px;
    }

    /* ---------- CHAT ---------- */

    .chat-info {
        border-radius: 15px;
        padding: 15px;
        border: 1px solid rgba(128,128,128,0.18);
        margin-bottom: 20px;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        opacity: 0.5;
        margin-top: 50px;
        padding: 25px;
        font-size: 0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# EVENT DATA
# ============================================================

EVENTS = [
    {
        "id": 1,
        "name": "Tech Innovation Summit 2026",
        "category": "Technology",
        "emoji": "💻",
        "date": "October 10, 2026",
        "time": "10:00 AM",
        "location": "Mumbai Convention Centre",
        "price": 999,
        "available": 120,
        "description": (
            "Explore AI, robotics, cloud computing, cybersecurity "
            "and the future of technology."
        ),
    },
    {
        "id": 2,
        "name": "Mumbai Music Festival",
        "category": "Music",
        "emoji": "🎵",
        "date": "October 18, 2026",
        "time": "6:00 PM",
        "location": "Jio World Garden, Mumbai",
        "price": 1499,
        "available": 250,
        "description": (
            "A spectacular evening of live music, artists, "
            "performances and entertainment."
        ),
    },
    {
        "id": 3,
        "name": "Startup & Business Expo",
        "category": "Business",
        "emoji": "💼",
        "date": "November 2, 2026",
        "time": "9:30 AM",
        "location": "Bandra Exhibition Centre",
        "price": 799,
        "available": 180,
        "description": (
            "Connect with entrepreneurs, investors, founders "
            "and business leaders."
        ),
    },
    {
        "id": 4,
        "name": "Food & Culture Festival",
        "category": "Food",
        "emoji": "🍔",
        "date": "November 15, 2026",
        "time": "12:00 PM",
        "location": "Nesco Grounds, Mumbai",
        "price": 499,
        "available": 500,
        "description": (
            "Discover food, culture, live cooking and entertainment "
            "from across India."
        ),
    },
    {
        "id": 5,
        "name": "Photography Masterclass",
        "category": "Workshop",
        "emoji": "📸",
        "date": "December 5, 2026",
        "time": "11:00 AM",
        "location": "Kala Ghoda, Mumbai",
        "price": 599,
        "available": 35,
        "description": (
            "A hands-on photography masterclass for beginners "
            "and experienced photographers."
        ),
    },
    {
        "id": 6,
        "name": "Stand-Up Comedy Night",
        "category": "Comedy",
        "emoji": "😂",
        "date": "December 12, 2026",
        "time": "8:00 PM",
        "location": "The Comedy Club, Mumbai",
        "price": 699,
        "available": 90,
        "description": (
            "Spend an evening laughing with some of the city's "
            "best stand-up comedians."
        ),
    },
]


# ============================================================
# SESSION STATE
# ============================================================

if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 **Welcome to EventHub!**\n\n"
                "I can help you discover events, check prices, "
                "find venues and manage your bookings. 🎟️\n\n"
                "Try asking **'What events are available?'**"
            ),
            "time": datetime.now().strftime("%I:%M %p"),
        }
    ]

if "selected_event" not in st.session_state:
    st.session_state.selected_event = None


# ============================================================
# FUNCTIONS
# ============================================================

def get_event(event_id):
    """Return event by ID."""

    for event in EVENTS:
        if event["id"] == event_id:
            return event

    return None


def get_time():
    """Return current time."""

    return datetime.now().strftime("%I:%M %p")


def create_booking(event, quantity, customer_name, email):
    """Create a new booking."""

    booking_id = (
        f"EH{datetime.now().strftime('%y%m%d')}"
        f"{random.randint(1000, 9999)}"
    )

    booking = {
        "id": booking_id,
        "event_id": event["id"],
        "event": event["name"],
        "date": event["date"],
        "time": event["time"],
        "location": event["location"],
        "tickets": quantity,
        "price": event["price"],
        "total": event["price"] * quantity,
        "name": customer_name,
        "email": email,
        "status": "Confirmed",
        "created": datetime.now().strftime(
            "%d %b %Y, %I:%M %p"
        ),
    }

    st.session_state.bookings.append(booking)

    event["available"] -= quantity

    return booking


def cancel_booking(booking_id):
    """Cancel a booking and restore ticket inventory."""

    for booking in st.session_state.bookings:

        if booking["id"] == booking_id:

            if booking["status"] == "Cancelled":
                return False

            event = get_event(booking["event_id"])

            if event:
                event["available"] += booking["tickets"]

            booking["status"] = "Cancelled"

            return True

    return False


def event_list_text(events):
    """Format events for chatbot."""

    if not events:
        return "I couldn't find any matching events. 😕"

    text = "### 🎟️ Events\n\n"

    for event in events:
        text += (
            f"**{event['emoji']} {event['name']}**\n"
            f"📅 {event['date']} • ⏰ {event['time']}\n"
            f"📍 {event['location']}\n"
            f"💰 ₹{event['price']} per ticket\n\n"
        )

    return text


def chatbot_response(user_input):
    """Handle event assistant conversations."""

    message = user_input.lower().strip()

    # Greeting
    if any(
        word in message
        for word in ["hello", "hi", "hey"]
    ):
        return (
            "Hello! 👋 Welcome to **EventHub**.\n\n"
            "Would you like to discover some events? 🎟️"
        )

    # All events
    if (
        "all events" in message
        or "available events" in message
        or "what events" in message
        or message == "events"
        or "show events" in message
    ):
        return event_list_text(EVENTS)

    # Categories
    categories = {
        "technology": "Technology",
        "tech": "Technology",
        "music": "Music",
        "business": "Business",
        "startup": "Business",
        "food": "Food",
        "workshop": "Workshop",
        "photography": "Workshop",
        "comedy": "Comedy",
    }

    for keyword, category in categories.items():

        if keyword in message:

            matching = [
                event
                for event in EVENTS
                if event["category"] == category
            ]

            if matching:
                return event_list_text(matching)

    # Price
    if (
        "price" in message
        or "cost" in message
        or "how much" in message
    ):

        for event in EVENTS:

            if (
                event["name"].lower()
                in message
            ):
                return (
                    f"🎟️ **{event['name']}**\n\n"
                    f"Ticket price: **₹{event['price']}**"
                )

        return (
            "Sure! 💰 Which event's price would you "
            "like to know?"
        )

    # Location
    if (
        "where" in message
        or "venue" in message
        or "location" in message
    ):

        for event in EVENTS:

            if any(
                word in message
                for word in event["name"].lower().split()
                if len(word) > 4
            ):
                return (
                    f"📍 **{event['name']}**\n\n"
                    f"Venue: **{event['location']}**"
                )

        return (
            "Which event are you asking about? 📍 "
            "Tell me its name."
        )

    # Booking
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
            "🎟️ Ready to book?\n\n"
            "Choose an event from the **Book Tickets** "
            "section in the sidebar, select your ticket "
            "quantity, enter your details and confirm."
        )

    # My bookings
    if (
        "my bookings" in message
        or "my booking" in message
    ):

        if not st.session_state.bookings:
            return (
                "You don't have any bookings yet. 🎟️"
            )

        result = "### 📋 Your Bookings\n\n"

        for booking in st.session_state.bookings:

            result += (
                f"**{booking['id']}** — "
                f"{booking['event']}\n"
                f"🎫 {booking['tickets']} ticket(s) • "
                f"₹{booking['total']} • "
                f"{booking['status']}\n\n"
            )

        return result

    # Cancellation
    if "cancel" in message:

        return (
            "❌ To cancel a booking, open **My Bookings** "
            "in the sidebar and select the booking you "
            "want to cancel."
        )

    # Help
    if "help" in message:

        return (
            "### 🤖 EventHub Assistant\n\n"
            "I can help you:\n\n"
            "🎟️ Find events\n\n"
            "💰 Check ticket prices\n\n"
            "📍 Find event venues\n\n"
            "🎫 Book tickets\n\n"
            "📋 View your bookings\n\n"
            "❌ Cancel bookings"
        )

    # Thanks
    if (
        "thanks" in message
        or "thank you" in message
    ):
        return (
            "You're very welcome! 😊\n\n"
            "Have a fantastic time at your event! 🎉"
        )

    # Goodbye
    if (
        message == "bye"
        or "goodbye" in message
    ):
        return (
            "Goodbye! 👋\n\n"
            "See you at EventHub! 🎟️"
        )

    # Fallback
    return (
        "I'm not sure I understood that. 🤔\n\n"
        "Try asking:\n\n"
        "• **What events are available?**\n"
        "• **Show me music events**\n"
        "• **What is the ticket price?**\n"
        "• **Where is the event?**\n"
        "• **How do I book tickets?**"
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎟️ EventHub")

    st.caption(
        "Discover. Book. Enjoy."
    )

    st.divider()

    # --------------------------------------------------------
    # QUICK NAVIGATION
    # --------------------------------------------------------

    st.subheader("🧭 Navigation")

    page = st.radio(
        "Go to",
        [
            "🏠 Discover Events",
            "🎫 Book Tickets",
            "📋 My Bookings",
            "🤖 Event Assistant",
        ],
        label_visibility="collapsed",
    )

    st.divider()

    # --------------------------------------------------------
    # BOOKING FORM
    # --------------------------------------------------------

    if page == "🎫 Book Tickets":

        st.subheader("🎟️ Book Tickets")

        available_events = [
            event
            for event in EVENTS
            if event["available"] > 0
        ]

        if available_events:

            event_names = [
                event["name"]
                for event in available_events
            ]

            selected_name = st.selectbox(
                "Select event",
                event_names,
            )

            selected = next(
                event
                for event in available_events
                if event["name"] == selected_name
            )

            st.info(
                f"📅 {selected['date']}\n\n"
                f"📍 {selected['location']}\n\n"
                f"🎟️ ₹{selected['price']} / ticket"
            )

            quantity = st.number_input(
                "Number of tickets",
                min_value=1,
                max_value=min(
                    10,
                    selected["available"]
                ),
                value=1,
            )

            name = st.text_input(
                "Full name",
                placeholder="Your name",
            )

            email = st.text_input(
                "Email address",
                placeholder="you@example.com",
            )

            total = (
                selected["price"]
                * quantity
            )

            st.metric(
                "Total Amount",
                f"₹{total:,}",
            )

            if st.button(
                "🎟️ Confirm Booking",
                type="primary",
                use_container_width=True,
            ):

                if not name.strip():
                    st.error(
                        "Please enter your name."
                    )

                elif (
                    "@" not in email
                    or "." not in email
                ):
                    st.error(
                        "Please enter a valid email."
                    )

                else:

                    booking = create_booking(
                        selected,
                        quantity,
                        name,
                        email,
                    )

                    st.success(
                        "🎉 Booking Confirmed!"
                    )

                    st.write(
                        f"**Booking ID:** "
                        f"`{booking['id']}`"
                    )

        else:

            st.warning(
                "No tickets are currently available."
            )

    # --------------------------------------------------------
    # MY BOOKINGS
    # --------------------------------------------------------

    if page == "📋 My Bookings":

        st.subheader("📋 My Bookings")

        if not st.session_state.bookings:

            st.info(
                "You don't have any bookings yet."
            )

        else:

            for booking in st.session_state.bookings:

                with st.container(border=True):

                    st.write(
                        f"🎟️ **{booking['event']}**"
                    )

                    st.caption(
                        f"Booking ID: {booking['id']}"
                    )

                    st.write(
                        f"📅 {booking['date']}"
                    )

                    st.write(
                        f"📍 {booking['location']}"
                    )

                    st.write(
                        f"🎫 Tickets: "
                        f"{booking['tickets']}"
                    )

                    st.write(
                        f"💰 Total: "
                        f"₹{booking['total']:,}"
                    )

                    if booking["status"] == "Confirmed":

                        if st.button(
                            "❌ Cancel Booking",
                            key=f"cancel_{booking['id']}",
                            use_container_width=True,
                        ):

                            cancel_booking(
                                booking["id"]
                            )

                            st.rerun()

                    else:

                        st.warning(
                            "Booking Cancelled"
                        )

    # --------------------------------------------------------
    # QUICK STATS
    # --------------------------------------------------------

    st.divider()

    st.subheader("📊 Statistics")

    total_bookings = len(
        st.session_state.bookings
    )

    confirmed = sum(
        1
        for booking
        in st.session_state.bookings
        if booking["status"] == "Confirmed"
    )

    st.metric(
        "My Bookings",
        total_bookings,
    )

    st.metric(
        "Confirmed",
        confirmed,
    )


# ============================================================
# DISCOVER EVENTS PAGE
# ============================================================

if page == "🏠 Discover Events":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                🎟️ Discover Amazing Events
            </div>

            <div class="hero-text">
                Find your next experience, connect with people,
                and book your tickets in seconds.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    search = st.text_input(
        "🔎 Search events",
        placeholder=(
            "Search by event name, category or location..."
        ),
    )

    # --------------------------------------------------------
    # CATEGORY FILTER
    # --------------------------------------------------------

    categories = [
        "All",
        "Technology",
        "Music",
        "Business",
        "Food",
        "Workshop",
        "Comedy",
    ]

    selected_category = st.selectbox(
        "📂 Category",
        categories,
    )

    # --------------------------------------------------------
    # FILTER EVENTS
    # --------------------------------------------------------

    filtered_events = EVENTS.copy()

    if selected_category != "All":

        filtered_events = [
            event
            for event in filtered_events
            if event["category"]
            == selected_category
        ]

    if search:

        search_lower = search.lower()

        filtered_events = [
            event
            for event in filtered_events
            if (
                search_lower
                in event["name"].lower()
                or search_lower
                in event["category"].lower()
                or search_lower
                in event["location"].lower()
            )
        ]

    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    st.write(
        f"**{len(filtered_events)} event(s) found**"
    )

    if not filtered_events:

        st.warning(
            "No events match your search."
        )

    else:

        columns = st.columns(3)

        for index, event in enumerate(
            filtered_events
        ):

            with columns[index % 3]:

                st.markdown(
                    f"""
                    <div class="event-card">

                        <div class="event-category">
                            {event['emoji']}
                            {event['category']}
                        </div>

                        <div class="event-name">
                            {event['name']}
                        </div>

                        <div class="event-detail">
                            📅 {event['date']}
                        </div>

                        <div class="event-detail">
                            ⏰ {event['time']}
                        </div>

                        <div class="event-detail">
                            📍 {event['location']}
                        </div>

                        <div class="event-price">
                            ₹{event['price']:,}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "🎟️ Book This Event",
                    key=f"book_{event['id']}",
                    use_container_width=True,
                ):

                    st.session_state.selected_event = (
                        event["id"]
                    )

                    st.info(
                        "Go to **🎫 Book Tickets** "
                        "in the sidebar to complete your booking."
                    )


# ============================================================
# EVENT ASSISTANT PAGE
# ============================================================

if page == "🤖 Event Assistant":

    st.markdown(
        """
        <div class="chat-info">

        ### 🤖 EventHub Assistant

        I can help you find events, check ticket prices,
        locate venues and manage your bookings.

        </div>
        """,
        unsafe_allow_html=True,
    )

    # Display messages

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

            st.caption(
                message["time"]
            )

    # Chat input

    user_input = st.chat_input(
        "Ask about events, tickets or bookings..."
    )

    if user_input:

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

        # Generate response

        with st.chat_message("assistant"):

            with st.spinner(
                "Checking EventHub... 🔎"
            ):
                time.sleep(0.5)

            response = chatbot_response(
                user_input
            )

            st.markdown(
                response
            )

            st.caption(
                get_time()
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
                "time": get_time(),
            }
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        🎟️ <strong>EventHub</strong><br>
        Discover • Book • Enjoy<br><br>
        Built with ❤️ using Python & Streamlit

    </div>
    """,
    unsafe_allow_html=True,
)

