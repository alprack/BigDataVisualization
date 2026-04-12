import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/tsla.us.txt")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Close"])
plt.title("Tesla Stock Price - Raw Data")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.tight_layout()
plt.show()