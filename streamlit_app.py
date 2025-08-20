import streamlit as st

# --- CSS to hide sidebar if not logged in ---
def hide_sidebar():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Login check ---
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        hide_sidebar()  # hide sidebar before login
        st.title("🔒 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "Karan" and password == "1234":
                st.session_state["logged_in"] = True
                st.success("✅ Login successful")
                st.rerun()  # << fix here
            else:
                st.error("Invalid credentials")

        st.stop()  # stop execution here until login


check_login()

# --- After login ---
st.title("🏠 Welcome")
st.write("Use the sidebar to navigate pages once logged in.")
