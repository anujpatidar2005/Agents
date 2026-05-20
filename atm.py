import streamlit as st

# Initial data
if "data" not in st.session_state:
    st.session_state.data = {12345: [None, 10000]}
    st.session_state.pin = None

st.title("🏦 Welcome to SBI")

# Main menu
option = st.selectbox(
    "Choose option:",
    [
        "Pin Generation",
        "Cash Withdrawal",
        "Cash Deposit",
        "Check Balance",
        "Exit",
    ],
)

# PIN Generation
if option == "Pin Generation":
    pin = st.text_input("Enter 4 digit PIN", type="password")
    if st.button("Generate PIN"):
        st.session_state.pin = pin
        st.success("PIN Generated Successfully ✅")

# Cash Withdrawal
elif option == "Cash Withdrawal":
    if st.session_state.pin is None:
        st.warning("Please generate PIN first ⚠️")
    else:
        amount = st.number_input("Enter amount", min_value=0)
        if st.button("Withdraw"):
            if amount <= st.session_state.data[12345][1]:
                st.session_state.data[12345][1] -= amount
                st.success(
                    f"Transaction successful ✅ Remaining balance: {st.session_state.data[12345][1]}"
                )
            else:
                st.error("Insufficient balance ❌")

# Cash Deposit
elif option == "Cash Deposit":
    if st.session_state.pin is None:
        st.warning("Please generate PIN first ⚠️")
    else:
        amount = st.number_input("Enter amount", min_value=0)
        if st.button("Deposit"):
            st.session_state.data[12345][1] += amount
            st.success(
                f"Deposit successful ✅ Remaining balance: {st.session_state.data[12345][1]}"
            )

# Check Balance
elif option == "Check Balance":
    if st.session_state.pin is None:
        st.warning("Please generate PIN first ⚠️")
    else:
        st.info(f"Your balance is: {st.session_state.data[12345][1]}")

# Exit
elif option == "Exit":
    st.write("Thank you for using SBI 😊")