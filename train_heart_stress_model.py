# Filename: train_heart_stress_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# ----------------------------
# Step 1: Load dataset
# ----------------------------
data_path = r"C:\Users\Admin\Desktop\LAASHYA\EMBEDDED PEP\PROJECT\VSC_2\data\wesad_features_dataset.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Dataset not found at {data_path}")

df = pd.read_csv(data_path)
print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)
print(df.head())

# ----------------------------
# Step 2: Prepare features and labels
# ----------------------------
X = df.drop(columns=['participant', 'label'])
y = df['label']

# ----------------------------
# Step 3: Split into train and test sets
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {X_train.shape[0]}, Testing samples: {X_test.shape[0]}")

# ----------------------------
# Step 4: Train Random Forest classifier
# ----------------------------
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# ----------------------------
# Step 5: Evaluate the model
# ----------------------------
y_pred = clf.predict(X_test)

print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ----------------------------
# Step 6: Save the trained model
# ----------------------------
model_path = r"C:\Users\Admin\Desktop\LAASHYA\EMBEDDED PEP\PROJECT\VSC_2\rf_heart_stress_model.pkl"
joblib.dump(clf, model_path)
print(f"\nTrained model saved at: {model_path}")
