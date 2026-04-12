import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/tsla.us.txt")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

st.title("Interactive Visualization of Tesla Stock Data")

start_date = st.date_input("Start Date", df["Date"].min().date())
end_date = st.date_input("End Date", df["Date"].max().date())

filtered_df = df[
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

mode = st.selectbox("Choose View", ["Raw", "Sampled", "Monthly Aggregated"])

if mode == "Sampled":
    filtered_df = filtered_df.iloc[::10]
elif mode == "Monthly Aggregated":
    filtered_df = filtered_df.resample("ME", on="Date").mean(numeric_only=True).reset_index()

fig = px.line(filtered_df, x="Date", y="Close", title=f"{mode} Tesla Closing Price")
st.plotly_chart(fig, use_container_width=True)

st.write("Rows displayed:", len(filtered_df))