import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

BASE_DIR = "data"
TRAIN_DIR = os.path.join(BASE_DIR, "TRAIN")
OUTPUT_DATASET = os.path.join(BASE_DIR, "wesad_features_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "rf_heart_stress_model.pkl")

# ---------------- FEATURE EXTRACTION ----------------
def extract_features_from_participant(participant_path, label):
    features = {}
    
    # --- List of expected CSVs and their feature names ---
    csv_files = {
        "IBI.csv": ["mean_ibi", "std_ibi"],
        "HR.csv": ["mean_hr", "std_hr"],
        "ACC.csv": ["mean_acc", "std_acc"]
    }

    try:
        for csv_file, feature_names in csv_files.items():
            file_path = os.path.join(participant_path, csv_file)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                values = df.iloc[:, 1].astype(float)  # use second column
                features[feature_names[0]] = values.mean()
                features[feature_names[1]] = values.std()
            else:
                # if file is missing, fill features with NaN
                features[feature_names[0]] = np.nan
                features[feature_names[1]] = np.nan

        # Add label and participant ID
        features["label"] = label
        features["participant"] = os.path.basename(participant_path)

        return features

    except Exception as e:
        print(f"Skipping {participant_path}: {e}")
        return None

     

    except Exception as e:
        print(f"Skipping {participant_path}: {e}")
        return None


# ---------------- DATASET CREATION ----------------
rows = []

for class_name, label in [("BASELINE", 0), ("STRESS", 1)]:
    class_path = os.path.join(TRAIN_DIR, class_name)
    print(f"\nLooking in: {class_path}")

    if not os.path.exists(class_path):
        print("❌ Folder does not exist")
        continue

    for participant in os.listdir(class_path):
        participant_path = os.path.join(class_path, participant)
        print(f"  Found participant folder: {participant_path}")

        if not os.path.isdir(participant_path):
            print("  ❌ Not a directory")
            continue

        feats = extract_features_from_participant(participant_path, label)

        if feats:
            print("  ✅ Features extracted")
            rows.append(feats)
        else:
            print("  ❌ Feature extraction failed")


df = pd.DataFrame(rows)

if df.empty:
    raise ValueError("❌ Dataset is empty. Check folder names and CSV files.")

df.to_csv(OUTPUT_DATASET, index=False)
print(f"\nDataset saved at {OUTPUT_DATASET}")

# ---------------- MODEL TRAINING ----------------
X = df.drop(columns=["label", "participant"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

joblib.dump(clf, MODEL_PATH)
print(f"\nTrained model saved at {MODEL_PATH}")
