import streamlit as st

# --- Login check ---
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        st.title("🔒 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if (
                username == "Karan"
                and password == "1234"
            ):
                st.session_state["logged_in"] = True
                st.success("✅ Login successful")
                st.experimental_rerun()
            else:
                st.error("Invalid credentials")

        st.stop()  # stop execution here until login

check_login()

st.title("🏠 Welcome")
st.write("Use the sidebar to navigate pages once logged in.")
