import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import datetime

# -----------------------------
# Firebase Initialization
# -----------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["FIREBASE_SERVICE_ACCOUNT"]))
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://karanexports-d7f67.firebaseio.com/"
    })

# -----------------------------
# UI: Order Form
# -----------------------------
st.title("📦 Add New Order")

customer = st.text_input("Customer Name")
billing = st.text_area("Billing Address")
shipping = st.text_area("Shipping Address")
notes = st.text_area("Special Notes")

# -----------------------------
# Line Items
# -----------------------------
if "items" not in st.session_state:
    st.session_state["items"] = []

st.subheader("Line Items")

with st.form("item_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        design = st.text_input("Design")
        quality = st.text_input("Quality")
        size = st.text_input("Size (e.g. 6x9 ft)")
    with col2:
        qty = st.number_input("Pieces", min_value=1, step=1)
        instructions = st.text_input("Item Instructions")

    add_item = st.form_submit_button("➕ Add Item")

    if add_item:
        if design and quality and size:
            st.session_state["items"].append({
                "design": design,
                "quality": quality,
                "size": size,
                "qty": qty,
                "instructions": instructions
            })
        else:
            st.warning("⚠️ Please fill in Design, Quality, and Size before adding.")

# -----------------------------
# Show Current Items
# -----------------------------
if st.session_state["items"]:
    st.write("### Current Items")
    st.table(st.session_state["items"])

# -----------------------------
# Save Order
# -----------------------------
if st.button("💾 Save Order"):
    if not customer.strip():
        st.error("Customer name is required!")
    else:
        order = {
            "customer": customer,
            "billing_address": billing,
            "shipping_address": shipping,
            "notes": notes,
            "date": datetime.datetime.now().isoformat(),
            "status": "draft",
            "items": st.session_state["items"],
        }
        orders_ref = db.reference("orders")
        orders_ref.push(order)
        st.success("✅ Order saved to Firebase!")
        st.session_state["items"] = []  # reset
