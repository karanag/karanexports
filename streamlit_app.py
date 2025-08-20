import streamlit as st

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        # Hide sidebar until login
        st.markdown(
            "<style>[data-testid='stSidebar'] {display: none;}</style>",
            unsafe_allow_html=True,
        )
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

check_login()

# After login
st.title("🏠 Welcome")

# Show sidebar only after login, and no default "Navigation" text
with st.sidebar:
    st.header("📂 Pages")
    st.page_link("streamlit_app.py", label="🏠 Home")
    st.page_link("pages/1_Dashboard.py", label="📊 Dashboard")
    st.page_link("pages/2_Orders.py", label="📝 Orders")
    st.button("🚪 Logout", on_click=lambda: st.session_state.clear() or st.rerun())
