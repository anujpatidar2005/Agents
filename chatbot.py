import streamlit as st

st.title("🤖 AI Chat Bot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user = st.text_input("You:")

if st.button("Send"):
    if user:
        st.session_state.messages.append(("You", user))

        # Bot response logic
        if user.lower() in ["hii", "hello", "hey", "namstey", "he"]:
            response = "Hello Human! How may I help you?"

        elif "python" in user.lower():
            response = """Python is a high-level, general-purpose programming language known for its clear, readable syntax.
It supports multiple programming paradigms."""
        
        elif "data science" in user.lower():
            response = """Data science is a field that uses scientific methods, algorithms, and programming to extract insights from data."""

        elif user.lower() in ["yes", "no"]:
            response = "Thanks for your valuable feedback!"

        elif user.lower() in ["exit", "end", "close", "quit", "band", "bye"]:
            response = "Bye Bye. Have a nice day!"

        else:
            response = "This is not in my domain. Try another prompt."

        st.session_state.messages.append(("Bot", response))

# Display chat
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.write(f"🧑 {msg}")
    else:
        st.write(f"🤖 {msg}")