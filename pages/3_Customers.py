import streamlit as st
from streamlit_app import check_login  # import your login check

check_login()  # enforce login

st.title("👥 Customers")

# --- Session state store for demo ---
if "customers" not in st.session_state:
    st.session_state["customers"] = [
        {"name": "Alice Johnson", "email": "alice@example.com", "phone": "9876543210"},
        {"name": "Bob Smith", "email": "bob@example.com", "phone": "9123456780"},
    ]

# --- UI toggle ---
mode = st.radio("Choose an action:", ["View Customers", "➕ Add New Customer"], horizontal=True)

# --- View customers ---
if mode == "View Customers":
    if not st.session_state["customers"]:
        st.info("No customers added yet.")
    else:
        for cust in st.session_state["customers"]:
            with st.container():
                st.markdown(
                    f"""
                    <div style="border:1px solid #ddd; border-radius:10px; padding:15px; margin-bottom:10px; background:#f9f9f9;">
                        <h4>{cust['name']}</h4>
                        <p><b>Email:</b> {cust['email']}<br>
                        <b>Phone:</b> {cust['phone']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# --- Add new customer ---
else:
    with st.form("add_customer_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        submitted = st.form_submit_button("✅ Add Customer")

        if submitted:
            if name.strip() and email.strip() and phone.strip():
                st.session_state["customers"].append(
                    {"name": name, "email": email, "phone": phone}
                )
                st.success(f"Customer {name} added!")
                st.rerun()
            else:
                st.error("Please fill all fields")
