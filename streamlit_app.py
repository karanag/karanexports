import streamlit as st

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if not st.session_state["logged_in"]:
        st.markdown("<style>[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)
        st.title("🔒 Login")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                if username == "Karan" and password == "1234":
                    st.session_state["logged_in"] = True
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        st.stop()
    else:
        st.title("Welcome to KE")

check_login()

st.markdown(
    """
    <style>
    section[data-testid="stSidebarNav"] > div:first-child {display: none;} /* app title */
    [data-testid="stSidebarNav"] div:has(> p) {display: none;} /* "Navigation / Choose..." */
    </style>
    """,
    unsafe_allow_html=True,
)