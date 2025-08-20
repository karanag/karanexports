import streamlit as st

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Show login form if not logged in
    if not st.session_state["logged_in"]:
        st.title("🔒 Login")

        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")

        if submitted:
            if username == "Karan" and password == "1234":
                st.session_state["logged_in"] = True
                st.success("✅ Login successful")
                st.rerun()   # use new API
            else:
                st.error("Invalid credentials")

        # stop execution until login
        st.stop()

check_login()

# --- After login ---
st.title("🏠 Welcome")
st.write("Use the sidebar to navigate pages once logged in.")
