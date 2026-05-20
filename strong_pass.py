import streamlit as st

st.title("Password Strength Checker")

# Password input field
password = st.text_input("Enter Password:", type="password")

if password:
    uppercase = False
    lowercase = False
    number = False
    special_characters = False

    for i in password:
        if i.isupper():
            uppercase = True
        if i.islower():
            lowercase = True
        if i.isdigit():
            number = True
        if i in "!@#$%*&^":
            special_characters = True

    if uppercase and lowercase and number and special_characters and len(password) >= 8:
        st.success("✅ Strong Password")
    else:
        st.error("❌ Weak Password")
        st.write("Password must contain:")
        st.write("- At least 1 uppercase letter")
        st.write("- At least 1 lowercase letter")
        st.write("- At least 1 number")
        st.write("- At least 1 special character (!@#$%*&^)")
        st.write("- Minimum 8 characters")