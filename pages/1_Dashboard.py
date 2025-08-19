import streamlit as st

# Protect page
if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("📊 Dashboard")
st.write("This is your dashboard skeleton. Add charts, stats, etc.")
