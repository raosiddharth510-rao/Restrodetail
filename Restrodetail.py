import pandas as pd
import streamlit as st

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="🍽️ Restaurant Order & Sales App", layout="centered")

st.title("🍴 Restaurant Order & Sales Dashboard")
st.write("Enter a weekday (e.g., Monday) to view all orders and total profit for that day.")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("data/restaurant_sales.csv")
    return df

df = load_data()

# --- User Input ---
day = st.text_input("Enter the day of the week (e.g., Monday):", "").capitalize()

# --- Logic ---
if day:
    if day in df["Day"].unique():
        st.subheader(f"📅 Orders for {day}")

        # Filter data
        filtered_df = df[df["Day"] == day]
        st.dataframe(filtered_df)

        # Calculate Profit
        total_profit = filtered_df["Profit"].sum()
        total_sales = filtered_df["Total_Sales"].sum()
        total_orders = filtered_df.shape[0]

        # Display KPIs
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
