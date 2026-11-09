
import streamlit as st

st.title("UPI Fraud Risk Screening")
st.caption("AAIT Project — Interactive Screening Prototype")

st.subheader("Transaction Details")

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"]
)

amount = st.number_input(
    "Transaction Amount",
    value=50000.0,
    step=1000.0
)

st.info("Screening rule: Amounts above 200,000 require review.")

def check_transaction(amount):
    if amount < 0:
        return "Invalid Amount"
    elif amount > 200000:
        return "Review Required"
    return "Normal"

if st.button("Check Transaction", type="primary"):
    result = check_transaction(amount)

    st.write(f"Transaction type: **{transaction_type}**")

    if result == "Invalid Amount":
        st.error("Invalid Amount: Enter a non-negative value.")
    elif result == "Review Required":
        st.warning("Review Required: Flag for human review.")
    else:
        st.success("Normal: Below the illustrative review threshold.")

st.caption("Academic demonstration only. No trained fraud model.")
