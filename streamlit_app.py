import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import json

RTDB_URL = "https://karanexports-d7f67-default-rtdb.asia-southeast1.firebasedatabase.app/"

# --- Load credentials from secrets (supports both table and JSON-string) ---
print(st.secrets)
if "FIREBASE" in st.secrets:
    cred_info = dict(st.secrets["FIREBASE"])        # TOML table → dict
else:
    st.error(f"Missing secrets. Found keys: {list(st.secrets.keys())}. "
             "Add either [FIREBASE] table or SERVICE_ACCOUNT_JSON to secrets.")
    st.stop()

# --- Init Firebase Admin ---
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_info)
    firebase_admin.initialize_app(cred, {"databaseURL": RTDB_URL})

st.success("✅ Firebase Initialized")

# --- Sanity test: write + read ---
try:
    ref = db.reference("debug_test")
    ref.set({"status": "ok"})
    st.write("Readback:", ref.get())
except Exception as e:
    st.error(f"❌ Firebase test failed: {e}")

# --- UI: Order form ---
st.title("📦 Add New Order")

customer = st.text_input("Customer Name")
billing = st.text_area("Billing Address")
shipping = st.text_area("Shipping Address")
notes = st.text_area("Special Notes")

if "items" not in st.session_state:
    st.session_state["items"] = []

st.subheader("Line Items")
with st.form("item_form", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        design = st.text_input("Design")
        quality = st.text_input("Quality")
        size = st.text_input("Size (e.g. 6x9 ft)")
    with c2:
        qty = st.number_input("Pieces", min_value=1, step=1)
        instructions = st.text_input("Item Instructions")
    if st.form_submit_button("➕ Add Item"):
        if design and quality and size:
            st.session_state["items"].append({
                "design": design, "quality": quality, "size": size,
                "qty": qty, "instructions": instructions
            })
        else:
            st.warning("⚠️ Fill Design, Quality, Size.")

if st.session_state["items"]:
    st.write("### Current Items")
    st.table(st.session_state["items"])

if st.button("💾 Save Order"):
    if not customer.strip():
        st.error("Customer name is required!")
    else:
        order = {
            "customer": customer,
            "billing_address": billing,
            "shipping_address": shipping,
            "notes": notes,
            "date": datetime.now().isoformat(),
            "status": "draft",
            "items": st.session_state["items"],
        }
        db.reference("orders").push(order)
        st.success("✅ Order saved to Firebase!")
        st.session_state["items"] = []
