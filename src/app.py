import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Visualization of Stock Data")

# File upload
uploaded_file = st.file_uploader("Upload your dataset (CSV/TXT format)", type=["csv", "txt"])

# Load dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using default Tesla dataset")
    df = pd.read_csv("data/tsla.us.txt")

# 🔴 REQUIRED COLUMN CHECK
required_columns = ["Date", "Close"]

if not all(col in df.columns for col in required_columns):
    st.error("Uploaded file must contain 'Date' and 'Close' columns.")
    st.stop()

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# ⭐ BONUS: column selection
value_column = st.selectbox("Select value column", df.columns, index=list(df.columns).index("Close"))

# Date filter
start_date = st.date_input("Start Date", df["Date"].min().date())
end_date = st.date_input("End Date", df["Date"].max().date())

filtered_df = df[
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

# Mode selection
mode = st.selectbox(
    "Choose View",
    ["Raw", "Sampled", "Monthly Aggregated"]
)

# Apply techniques
if mode == "Sampled":
    filtered_df = filtered_df.iloc[::10]

elif mode == "Monthly Aggregated":
    filtered_df = filtered_df.resample("ME", on="Date").mean(numeric_only=True).reset_index()

# Plot
fig = px.line(
    filtered_df,
    x="Date",
    y=value_column,
    title=f"{mode} Visualization ({value_column})"
)

st.plotly_chart(fig, use_container_width=True)

# Info
st.write("Rows displayed:", len(filtered_df))