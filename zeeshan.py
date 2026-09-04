
import streamlit as st

st.set_page_config(page_title="Event Registration", page_icon="🎉")
st.title("🎉 Event Registration Form")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

event = st.selectbox("Choose Event", [
    "Tech Workshop",
    "Cybersecurity Seminar",
    "Cloud Computing Meetup",
    "Coding Competition",
    "AI & Machine Learning Workshop"
])

date = st.date_input("Event Date")
guests = st.number_input("Number of Guests", 1, 10, 1)
mode = st.radio("Event Mode", ["Online", "Offline"])
agree = st.checkbox("I agree to the terms and conditions")

if st.button("🎟️ Register"):
    if not name or not email or not phone:
        st.error("Please fill in all details.")
    elif not agree:
        st.warning("Please agree to the terms.")
    else:
        st.success("🎉 Registration Successful!")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Event:", event)
        st.write("Date:", date)
        st.write("Guests:", guests)
        st.write("Mode:", mode)