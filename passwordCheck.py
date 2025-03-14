import streamlit as st
import re
import string
import random

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# Function to evaluate password strength
def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ **Password should be at least 8 characters long.**")
    
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("❌ **Password should contain both uppercase and lowercase letters.**")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("❌ **Password should contain at least one digit.**")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ **Password should contain at least one special character (!@#$%^&*).**")
    
    if score == 4:
        strength = "✅ **Strong**"
        feedback.append("✅ **Your password is strong! No changes needed.**")
    elif score == 3:
        strength = "🟡 **Moderate**"
        feedback.append("🔹 **Your password is moderate. Consider adding more complexity.**")
    else:
        strength = "❌ **Weak**"
        feedback.append("⚠️ **Your password is weak. Please follow the suggestions to strengthen it.**")
    
    return strength, feedback

# Function to generate a strong random password
def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(all_characters) for _ in range(length))

# Streamlit UI
st.title("🔒 How Secure Is My Password?")
st.markdown("✅ **The #1 Password Strength Checker Tool.**")

# Password input
password_input = st.text_input("Enter your password:", type="password", placeholder="Type here...")

if st.button("Check Password Strength"):
    if password_input:
        strength, feedback = evaluate_password(password_input)
        st.subheader(f"Password Strength: {strength}")

        for msg in feedback:
            st.markdown(msg)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")

st.markdown("---")

# Generate strong password
st.subheader("🔑 Need a Strong Password?")
password_length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12, step=1)

if st.button("Generate Password"):
    generated_password = generate_password(password_length)
    st.text_input("Suggested Strong Password:", generated_password)

st.markdown("🔹 **Note:** This tool does not store or transmit any data.")
