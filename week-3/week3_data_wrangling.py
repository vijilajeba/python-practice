# Week 3 Assignment: Python & Data Wrangling
# Libraries: pandas, numpy, matplotlib, seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read the CSV file
df = pd.read_csv("data.csv")
print("Original dataset shape:", df.shape)
print(df.head())

# 2. Clean column names and date formats
df.columns = df.columns.str.strip()
df["Date"] = df["Date"].astype("string").str.strip().str.strip("'")
df["Date"] = df["Date"].replace({"20201226": "2020/12/26", "": pd.NA, "nan": pd.NA})
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Handle missing values
# The missing date is inferred from the daily sequence in December 2020.
df["Date"] = df["Date"].fillna(pd.Timestamp("2020-12-22"))
# Median is used to fill missing Calories values.
df["Calories"] = df["Calories"].fillna(df["Calories"].median())

# 5. Filter invalid/unusual records
# Duration 450 appears to be a likely data-entry error.
df = df[(df["Duration"] > 0) & (df["Duration"] <= 120)]
# Pulse should not exceed Maxpulse in this dataset; inspect before excluding.
df = df[df["Pulse"] <= df["Maxpulse"]]

# 6. Create new columns
df["Calories_Per_Minute"] = (df["Calories"] / df["Duration"]).round(2)
df["Intensity"] = np.select(
    [df["Pulse"] < 100, df["Pulse"] < 110],
    ["Low", "Moderate"],
    default="High"
)

# 7. Sort, inspect, and save
df = df.sort_values("Date").reset_index(drop=True)
print("\\nCleaned dataset shape:", df.shape)
print("\\nMissing values after cleaning:\\n", df.isna().sum())
print(df.head())
df.to_csv("week3_cleaned_data.csv", index=False)

# 8. Matplotlib visualization: Duration vs Calories
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Calories"], marker="o")
plt.title("Calories Burned Over Time")
plt.xlabel("Date")
plt.ylabel("Calories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Seaborn visualization: Pulse distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Pulse", bins=8, kde=True)
plt.title("Distribution of Pulse")
plt.xlabel("Pulse")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# 10. Seaborn visualization: Calories by intensity
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Intensity", y="Calories")
plt.title("Calories by Pulse Intensity")
plt.xlabel("Intensity")
plt.ylabel("Calories")
plt.tight_layout()
plt.show()
