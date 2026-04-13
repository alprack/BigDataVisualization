import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

# Load dataset
df = pd.read_csv("data/tsla.us.txt")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create sampled and aggregated data
sampled_df = df.iloc[::10]
monthly_df = df.resample("ME", on="Date").mean(numeric_only=True)

# -------- RAW --------
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Close"])
plt.title("Tesla Stock Price - Raw Data")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.tight_layout()
plt.savefig("screenshots/raw_plot.png")
plt.close()

# -------- SAMPLED --------
plt.figure(figsize=(10, 5))
plt.plot(sampled_df["Date"], sampled_df["Close"])
plt.title("Tesla Stock Price - Sampled Data")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.tight_layout()
plt.savefig("screenshots/sampled_plot.png")
plt.close()

# -------- AGGREGATED --------
plt.figure(figsize=(10, 5))
plt.plot(monthly_df.index, monthly_df["Close"])
plt.title("Tesla Stock Price - Monthly Aggregated Data")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.tight_layout()
plt.savefig("screenshots/aggregated_plot.png")
plt.close()