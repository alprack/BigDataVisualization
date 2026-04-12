import pandas as pd
import time
import matplotlib.pyplot as plt

df = pd.read_csv("data/tsla.us.txt")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

sampled_df = df.iloc[::10]
monthly_df = df.resample("ME", on="Date").mean(numeric_only=True)

start = time.time()
plt.figure()
plt.plot(df["Date"], df["Close"])
plt.close()
raw_time = time.time() - start

start = time.time()
plt.figure()
plt.plot(sampled_df["Date"], sampled_df["Close"])
plt.close()
sampled_time = time.time() - start

start = time.time()
plt.figure()
plt.plot(monthly_df.index, monthly_df["Close"])
plt.close()
aggregated_time = time.time() - start

print("Raw time:", raw_time)
print("Sampled time:", sampled_time)
print("Aggregated time:", aggregated_time)
print("Raw rows:", len(df))
print("Sampled rows:", len(sampled_df))
print("Aggregated rows:", len(monthly_df))