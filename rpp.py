 

---

## 🌐 Project Overview

This project involves creating a web-based **Password Strength Meter** that evaluates the strength of a password based on its length, character diversity, and entropy. The application is built using **Python** and **Streamlit**, providing a simple and interactive user interface.

---

## 🛠️ Prerequisites

Before starting, ensure you have the following installed:

- ✅ **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- ✅ **Visual Studio Code (VS Code)**: [Download VS Code](https://code.visualstudio.com/)
- ✅ **Streamlit Library**: Install via pip

  ```bash
  pip install streamlit
  ```

---

## 🧱 Step-by-Step Guide

### 1. 📁 Set Up Your Project Directory

Open a terminal and run:

```bash
mkdir password_strength_meter
cd password_strength_meter
```

### 2. 📝 Create the Application Script

In your project directory, create a file named `app.py` and open it in VS Code. Add the following code:

```python
import streamlit as st
import math
import string

# Set up the page
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# Title of the app
st.title("🔐 Password Strength Meter")

# Function to calculate entropy
def calculate_entropy(password):
    charset_size = 0
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
    if any(c.isspace() for c in password):
        charset_size += 1
    return len(password) * math.log2(charset_size) if charset_size else 0

# Function to evaluate password strength
def evaluate_password_strength(password):
    entropy = calculate_entropy(password)
    if entropy < 28:
        return "Very Weak", "⚠️ Your password is too short! It must be at least 8 characters."
    elif entropy < 36:
        return "Weak", "⚠️ Weak: Can be cracked quickly. Use a stronger password."
    elif entropy < 60:
        return "Moderate", "✅ Moderate: Decent password, but can still be improved."
    elif entropy < 80:
        return "Strong", "✅ Strong: Hard to guess, but consider making it longer."
    else:
        return "Very Strong", "✅ Very Strong: Excellent password! Highly secure."

# User input
password = st.text_input("Enter your password:")

# Evaluate password strength
if password:
    strength, feedback = evaluate_password_strength(password)
    st.write(f"🔹 Strength: {strength}")
    st.write(f"🔹 Feedback: {feedback}")
```

### 3. 🚀 Run the Application

In the terminal, navigate to your project directory and run:

```bash
streamlit run app.py
```

This command will start the Streamlit server and open the application in your default web browser.

---

## 📦 Optional: Share Your Application

To share your application with others, you can deploy it using services like:

- 🌐 [Streamlit Cloud](https://streamlit.io/cloud)
- 🚀 [Render](https://render.com/)
- ☁️ [Heroku](https://www.heroku.com/)

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Panaversity Learn Modern AI Python Repository](https://github.com/panaversity/learn-modern-ai-python)

---

