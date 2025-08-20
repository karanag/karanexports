import streamlit as st

def hide_sidebar():
    hide_style = """
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        hide_sidebar()   # hide sidebar before login
        st.title("🔒 Login")

        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")

        if submitted:
            if username == "Karan" and password == "1234":
                st.session_state["logged_in"] = True
                st.success("✅ Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")
        st.stop()

check_login()

# --- After login ---
st.title("🏠 Welcome")
st.sidebar.title("Navigation")
st.sidebar.write("Choose a page here...")
