import streamlit as st
import random

st.title("🎮 Rock, Paper, Scissors Game")

# Initialize session state
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.user_points = 0
    st.session_state.comp_points = 0
    st.session_state.result = ""

# Show round
st.write(f"### Round {st.session_state.round} / 3")

# User choice
choice = st.radio(
    "Choose your move:",
    ["Rock (r)", "Paper (p)", "Scissor (s)"]
)

if st.button("Play"):
    user_choice = choice[0].lower()  # r, p, s
    comp_choice = random.choice(["r", "p", "s"])

    st.write(f"Computer selected: **{comp_choice}**")

    # Game logic
    if user_choice == comp_choice:
        result = "Tie 🤝"
    elif (user_choice == "r" and comp_choice == "s") or \
         (user_choice == "p" and comp_choice == "r") or \
         (user_choice == "s" and comp_choice == "p"):
        result = "You won this round 🎉"
        st.session_state.user_points += 1
    else:
        result = "Computer won this round 🤖"
        st.session_state.comp_points += 1

    st.session_state.result = result
    st.session_state.round += 1

# Show result
if st.session_state.result:
    st.success(st.session_state.result)

# Show score
st.write(f"### Score: You {st.session_state.user_points} - {st.session_state.comp_points} Computer")

# Final result after 3 rounds
if st.session_state.round > 3:
    if st.session_state.user_points > st.session_state.comp_points:
        st.balloons()
        st.success(f"🎉 Congratulations! You won the series {st.session_state.user_points}-{st.session_state.comp_points}")
    elif st.session_state.user_points < st.session_state.comp_points:
        st.error(f"😢 You lost! Computer won {st.session_state.comp_points}-{st.session_state.user_points}")
    else:
        st.info("🤝 It's a Tie Series!")

    # Restart button
    if st.button("Play Again 🔄"):
        st.session_state.round = 1
        st.session_state.user_points = 0
        st.session_state.comp_points = 0
        st.session_state.result = ""