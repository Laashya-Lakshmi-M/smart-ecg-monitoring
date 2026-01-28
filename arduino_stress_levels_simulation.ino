
/*
  Auto-generated Arduino Stress Simulation
  Prints stress levels and controls LED
  High stress → LED ON, Normal → LED OFF
  Predictions generated from ML model probabilities
*/

const int ledPin = 13; // Built-in LED

// Stress levels array
String stressLevels[] = {"Normal", "High", "High", "High"};
int numPredictions = 4;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Stress Level Simulation Started");
}

void loop() {
  for (int i = 0; i < numPredictions; i++) {
    String level = stressLevels[i];

    if (level == "High") {
      digitalWrite(ledPin, HIGH);  // Stress detected → LED ON
      Serial.println("Stress detected: HIGH");
    } else {
      digitalWrite(ledPin, LOW);   // Normal → LED OFF
      Serial.println("Stress: NORMAL");
    }

    delay(1000); // 1 second per prediction
  }

  // Stop after finishing the sequence
  while(true); 
}
