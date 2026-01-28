"""
Auto-generate Arduino sketch with stress levels based on ML model probabilities
Author: You
Description:
1. Load trained RandomForest ML model.
2. Load WESAD dataset features.
3. Predict stress probabilities.
4. Map probabilities to stress levels: "Normal" or "High".
5. Generate a complete Arduino sketch ready for simulation.
"""

import pandas as pd
import joblib

# -------------------- Paths --------------------
MODEL_PATH = "data/rf_heart_stress_model.pkl"
DATA_PATH = "data/wesad_features_dataset.csv"
OUTPUT_SKETCH = "arduino_stress_levels_simulation.ino"

# -------------------- Load ML model --------------------
clf = joblib.load(MODEL_PATH)

# -------------------- Load dataset --------------------
df = pd.read_csv(DATA_PATH)
X = df.drop(columns=["label", "participant"])

# -------------------- Predict stress probabilities --------------------
# Probability of stress (label = 1)
probabilities = clf.predict_proba(X)[:, 1]

# -------------------- Map probabilities to stress levels --------------------
# Threshold: <0.5 → Normal, >=0.5 → High
stress_levels = ["Normal" if p < 0.5 else "High" for p in probabilities]

# Convert to Arduino String array
arduino_array = ', '.join([f'"{s}"' for s in stress_levels])
num_predictions = len(stress_levels)

# -------------------- Generate Arduino sketch --------------------
arduino_code = f"""
/*
  Auto-generated Arduino Stress Simulation
  Prints stress levels and controls LED
  High stress → LED ON, Normal → LED OFF
  Predictions generated from ML model probabilities
*/

const int ledPin = 13; // Built-in LED

// Stress levels array
String stressLevels[] = {{{arduino_array}}};
int numPredictions = {num_predictions};

void setup() {{
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Stress Level Simulation Started");
}}

void loop() {{
  for (int i = 0; i < numPredictions; i++) {{
    String level = stressLevels[i];

    if (level == "High") {{
      digitalWrite(ledPin, HIGH);  // Stress detected → LED ON
      Serial.println("Stress detected: HIGH");
    }} else {{
      digitalWrite(ledPin, LOW);   // Normal → LED OFF
      Serial.println("Stress: NORMAL");
    }}

    delay(1000); // 1 second per prediction
  }}

  // Stop after finishing the sequence
  while(true); 
}}
"""

# -------------------- Save Arduino sketch --------------------
with open(OUTPUT_SKETCH, "w", encoding="utf-8") as f:
    f.write(arduino_code)

print(f"✅ Arduino sketch generated: {OUTPUT_SKETCH}")
print(f"Number of predictions: {num_predictions}")
print("Copy this file into Wokwi or Tinkercad to simulate stress levels.")
