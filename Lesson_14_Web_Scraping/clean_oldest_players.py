

import pandas as pd
import numpy as np

# Load the raw CSV file
df = pd.read_csv("csv_data/oldest_living_players.csv")

# Replace 'N/A' strings with NaN
df.replace(["N/A", ""], pd.NA, inplace=True)

# Drop rows where all values are NaN (optional)
df.dropna(how="all", inplace=True)

# Fill missing 'Name' and 'Team' with placeholder text
df["Name"] = df["Name"].fillna("Unknown")
df["Team"] = df["Team"].fillna("Unknown")

# Fill missing 'Birth Date', 'Debut', and 'Final Game' with empty strings
df["Birth Date"] = df["Birth Date"].fillna("")
df["Debut"] = df["Debut"].fillna("")
df["Final Game"] = df["Final Game"].fillna("")

# Fill missing 'Profile Link' with empty string
df["Profile Link"] = df["Profile Link"].fillna("")

# Save cleaned version
df.to_csv("oldest_living_players_cleaned.csv", index=False)

print("Cleaned CSV saved as 'oldest_living_players_cleaned.csv'")
