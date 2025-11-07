import pandas as pd
import streamlit as st

# --- Streamlit Page Setup ---
st.set_page_config(page_title="🍽️ Restaurant Order & Sales App", layout="centered")

st.title("🍴 Restaurant Order & Sales Dashboard")
st.write("Enter a weekday (e.g., Monday) to view all orders and total profit for that day.")

# --- Create Local DataFrame (No external file needed) ---
data = {
    "Day": ["Monday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Tuesday", "Friday"],
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Item": ["Burger", "Pizza", "Pasta", "Burger", "Fries", "Salad", "Steak", "Ice Cream", "Pizza", "Burger"],
    "Quantity": [5, 3, 4, 6, 8, 4, 3, 5, 2, 5],
    "Price": [10, 12, 11, 10, 5, 8, 20, 6, 12, 10],
    "Cost": [6, 7, 6, 6, 3, 4, 12, 3, 7, 6]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Quantity"] * df["Price"]
df["Profit"] = (df["Price"] - df["Cost"]) * df["Quantity"]

# --- User Input ---
day = st.text_input("Enter the day of the week (e.g., Monday):", "").capitalize()

# --- Logic ---
if day:
    if day in df["Day"].unique():
        st.subheader(f"📅 Orders for {day}")

        # Filter DataFrame
        filtered_df = df[df["Day"] == day]
        st.dataframe(filtered_df)

        # Calculate Profit
        total_profit = filtered_df["Profit"].sum()
        total_sales = filtered_df["Total_Sales"].sum()
        total_orders = filtered_df.shape[0]

        # KPIs
        st.metric("💰 Total Sales", f"${total_sales:,.2f}")
        st.metric("📈 Total Profit", f"${total_profit:,.2f}")
        st.metric("🧾 Total Orders", total_orders)

    else:
        st.error("❌ Invalid day. Please enter a valid weekday (e.g., Monday, Tuesday, ...).")
else:
    st.info("👆 Enter a day above to view orders and profit.")

# --- Optional Summary Chart ---
st.write("### 📊 Weekly Profit Summary")
summary = df.groupby("Day")["Profit"].sum().reset_index()
st.bar_chart(summary, x="Day", y="Profit")

st.caption("Built with ❤️ using Streamlit and Pandas")
