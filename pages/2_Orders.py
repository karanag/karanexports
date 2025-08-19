import streamlit as st

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("📦 Orders")
st.write("This page will later fetch & write data from Firebase.")
