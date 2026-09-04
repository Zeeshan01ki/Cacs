
print("🎉 Welcome to EventBot!")
print("Type 'bye' to exit.")

while True:
    a = input("You: ").lower()

    if a == "hi":
        print("Bot: Hello! How can I help you?")
    elif a == "events":
        print("Bot: Tech Workshop, Cybersecurity Seminar, Cloud Meetup.")
    elif a == "tech":
        print("Bot: Tech Workshop is available for all students.")
    elif a == "cyber":
        print("Bot: Cybersecurity Seminar covers basic security topics.")
    elif a == "cloud":
        print("Bot: Cloud Meetup focuses on AWS and Azure.")
    elif a == "date":
        print("Bot: Choose your event date during registration.")
    elif a == "mode":
        print("Bot: Events are available Online and Offline.")
    elif a == "bye":
        print("Bot: Goodbye! See you at the event! 🎟️")
        break
    else:
        print("Bot: Sorry, I don't understand.")