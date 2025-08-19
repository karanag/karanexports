import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import json

# Load from secrets
cred_dict = json.loads(st.secrets["SERVICE_ACCOUNT_JSON"])

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://karanexports-d7f67-default-rtdb.asia-southeast1.firebasedatabase.app/"
    })

st.success("✅ Firebase Initialized")

# Test
try:
    test_ref = db.reference("debug_test")
    test_ref.set({"status": "ok"})
    st.write("Readback:", test_ref.get())
except Exception as e:
    st.error(f"❌ Firebase test failed: {e}")
