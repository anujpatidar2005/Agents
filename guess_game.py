import streamlit as st
import random

st.title("🎯 Guessing Game (1 to 20)")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# User input
guess = st.number_input("Guess a number (1–20):", min_value=1, max_value=20, step=1)

if st.button("Check"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1

        if guess > st.session_state.number:
            st.warning("Bhai thoda chota socho 😅")
        elif guess < st.session_state.number:
            st.warning("Bhai thoda bada socho 😄")
        else:
            st.success(f"🎉 Correct guess in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        st.session_state.number = random.randint(1, 20)
        st.session_state.attempts = 0
        st.session_state.game_over = False