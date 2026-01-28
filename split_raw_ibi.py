import pandas as pd
import os

# Paths
RAW_FILE = "data/IBI.csv"
BASELINE_DIR = "data/TRAIN/BASELINE"
STRESS_DIR = "data/TRAIN/STRESS"

# Create folders if not exist
os.makedirs(BASELINE_DIR, exist_ok=True)
os.makedirs(STRESS_DIR, exist_ok=True)

# Load raw IBI data
df = pd.read_csv(RAW_FILE)

if df.empty:
    raise ValueError("❌ Raw IBI file is empty")

# Split ratio
split_index = int(0.6 * len(df))

baseline_df = df.iloc[:split_index]
stress_df = df.iloc[split_index:]

# Save files
baseline_df.to_csv(f"{BASELINE_DIR}/baseline_01.csv", index=False)
stress_df.to_csv(f"{STRESS_DIR}/stress_01.csv", index=False)

print("✅ Raw IBI split successfully")
print(f"Baseline samples: {len(baseline_df)}")
print(f"Stress samples: {len(stress_df)}")
