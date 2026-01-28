# Filename: comp_hrv_final.py

import pandas as pd
import numpy as np
import os

# ----------------------------
# Function to extract features from a single participant
# ----------------------------
def extract_features(file_paths):
    features = {}

    # ----------------------------
    # IBI
    # ----------------------------
    ibi_df = pd.read_csv(file_paths['ibi'])
    ibi_col = ibi_df.columns[-1]  # always take the last column
    features['mean_ibi'] = ibi_df[ibi_col].mean()
    features['std_ibi'] = ibi_df[ibi_col].std()
    features['min_ibi'] = ibi_df[ibi_col].min()
    features['max_ibi'] = ibi_df[ibi_col].max()

    # ----------------------------
    # HR
    # ----------------------------
    hr_df = pd.read_csv(file_paths['hr'])
    hr_col = hr_df.columns[-1]  # always take the last column
    features['mean_hr'] = hr_df[hr_col].mean()
    features['std_hr'] = hr_df[hr_col].std()
    features['min_hr'] = hr_df[hr_col].min()
    features['max_hr'] = hr_df[hr_col].max()

    # ----------------------------
    # ACC
    # ----------------------------
    acc_df = pd.read_csv(file_paths['acc'])
    if all(col in acc_df.columns for col in ['x','y','z']):
        acc_mag = np.sqrt(acc_df['x']**2 + acc_df['y']**2 + acc_df['z']**2)
        features['mean_acc'] = acc_mag.mean()
        features['std_acc'] = acc_mag.std()
        features['min_acc'] = acc_mag.min()
        features['max_acc'] = acc_mag.max()
    else:
        acc_col = acc_df.columns[-1]  # last column if x,y,z not present
        features['mean_acc'] = acc_df[acc_col].mean()
        features['std_acc'] = acc_df[acc_col].std()
        features['min_acc'] = acc_df[acc_col].min()
        features['max_acc'] = acc_df[acc_col].max()

    return features

# ----------------------------
# Main: process all participant folders
# ----------------------------
data_folder = r"C:\Users\Admin\Desktop\LAASHYA\EMBEDDED PEP\PROJECT\VSC_2\data"

dataset = []

# Loop through each participant folder
for participant in os.listdir(data_folder):
    participant_path = os.path.join(data_folder, participant)
    if os.path.isdir(participant_path):
        try:
            # Find files case-insensitively
            ibi_file = [f for f in os.listdir(participant_path) if 'ibi' in f.lower() and f.lower().endswith('.csv')][0]
            hr_file = [f for f in os.listdir(participant_path) if 'hr' in f.lower() and f.lower().endswith('.csv')][0]
            acc_file = [f for f in os.listdir(participant_path) if 'acc' in f.lower() and f.lower().endswith('.csv')][0]
            file_paths = {
                'ibi': os.path.join(participant_path, ibi_file),
                'hr': os.path.join(participant_path, hr_file),
                'acc': os.path.join(participant_path, acc_file)
            }
        except IndexError:
            print(f"Skipping {participant}: missing IBI, HR, or ACC file")
            continue

        feats = extract_features(file_paths)
        feats['participant'] = participant
        feats['label'] = 1  # example label; change based on real stress/baseline info
        dataset.append(feats)

# Convert to DataFrame
dataset_df = pd.DataFrame(dataset)
print("Final dataset:")
print(dataset_df)

# Save to CSV
dataset_csv_path = os.path.join(data_folder, "wesad_features_dataset.csv")
dataset_df.to_csv(dataset_csv_path, index=False)
print(f"\nDataset saved as '{dataset_csv_path}'")
