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

check_login()

# Sidebar nav (only once, custom)
with st.sidebar:
    st.header("📂 Pages")
    page = st.radio("Go to", ["🏠 Home", "📊 Dashboard", "📝 Orders"])
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# Render pages
if page == "🏠 Home":
    st.title("🏠 Welcome")
elif page == "📊 Dashboard":
    st.title("📊 Dashboard")
    st.write("Dashboard content here...")
elif page == "📝 Orders":
    st.title("📝 Orders")
    st.write("Orders page here...")
