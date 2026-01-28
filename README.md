## Smart ECG Monitoring 

ECG-Based Stress Monitoring Using Physiological Signals

## Abstract
This project presents an ECG-based stress monitoring system that analyzes multiple physiological signals to distinguish between baseline and stress conditions. The system utilizes biosignals such as Inter-Beat Interval (IBI), Heart Rate (HR), Electrodermal Activity (EDA), Blood Volume Pulse (BVP), Skin Temperature (TEMP), and Accelerometer (ACC) data. By extracting Heart Rate Variability (HRV) features and applying machine learning techniques, the system aims to support non-clinical stress monitoring for wearable healthcare applications.

---

## 1. Introduction
Stress significantly affects both physical and mental health. Continuous and non-invasive stress monitoring has become increasingly important in preventive healthcare and wearable technologies. ECG-derived parameters such as HR and HRV provide valuable insights into autonomic nervous system activity, making them reliable indicators of stress.

This project focuses on analyzing real-world physiological datasets to classify stress conditions and build a foundation for wearable stress monitoring systems.

---

## 2. Objectives
- To analyze ECG-derived parameters such as HR and IBI  
- To compute HRV features for stress assessment  
- To preprocess and organize multi-sensor physiological data  
- To classify baseline and stress conditions using machine learning  
- To support wearable and embedded health monitoring systems  

---

## 3. Physiological Signals Used
- **IBI (Inter-Beat Interval)** – derived from ECG, used for HRV analysis  
- **HR (Heart Rate)** – cardiovascular response indicator  
- **EDA (Electrodermal Activity)** – reflects sympathetic nervous system activity  
- **BVP (Blood Volume Pulse)** – related to blood flow and heart dynamics  
- **ACC (Accelerometer)** – motion and activity monitoring  
- **TEMP (Skin Temperature)** – influenced by stress-induced vasoconstriction  

---

## 4. Dataset Description
The project uses structured CSV-based physiological datasets containing recordings under baseline and stress conditions.


This modular architecture is suitable for both offline analysis and wearable embedded implementations.

---

## 6. Heart Rate Variability (HRV) Analysis

Heart Rate Variability (HRV) represents the variation in time intervals between consecutive heartbeats and is a key indicator of autonomic nervous system activity.

HRV is calculated using Inter-Beat Interval (IBI) values derived from ECG signals.

### 6.1 Time-Domain HRV Parameters

**Mean IBI**
\[
\text{Mean IBI} = \frac{1}{N} \sum_{i=1}^{N} IBI_i
\]

**SDNN (Standard Deviation of NN intervals)**
\[
SDNN = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (IBI_i - \overline{IBI})^2}
\]

**RMSSD (Root Mean Square of Successive Differences)**
\[
RMSSD = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N-1} (IBI_{i+1} - IBI_i)^2}
\]

### HRV Interpretation
- **Low HRV** → High stress  
- **High HRV** → Relaxed or baseline condition  

---

## 7. Machine Learning Model Description

### 7.1 Selected Model: Random Forest Classifier
Random Forest is an ensemble learning algorithm that constructs multiple decision trees and outputs the class based on majority voting.

#### Reasons for Selection:
- Handles non-linear physiological data efficiently  
- Robust against noise and outliers  
- Reduces overfitting compared to single decision trees  
- Suitable for multi-feature biomedical datasets  

---

### 7.2 Feature Set Used
- Mean Heart Rate  
- Inter-Beat Interval (IBI)  
- HRV features (SDNN, RMSSD)  
- Statistical features from EDA  
- BVP and Skin Temperature features  
- Motion-related features from Accelerometer  

---

### 7.3 Classification Output
The trained model classifies physiological input data into:
- **Baseline (No Stress)**
- **Stress Condition**

This output can be extended to real-time stress monitoring in wearable systems.

---

## 8. Embedded & Wearable Relevance
The proposed system can be adapted for wearable devices by optimizing signal preprocessing and feature extraction pipelines. Lightweight machine learning models can be deployed on embedded platforms, enabling on-device stress detection without continuous cloud dependency.

---

## 9. Applications
- Wearable stress monitoring systems  
- Non-clinical healthcare monitoring  
- Mental health and wellness analysis  
- Biomedical signal processing research  

---

## 10. Future Scope
- Real-time ECG acquisition using wearable sensors  
- Embedded system implementation (TinyML integration)  
- Advanced HRV frequency-domain analysis  
- Cloud-based dashboards and alerts  

---

## 11. Conclusion
This project demonstrates the effectiveness of ECG-based and multi-sensor physiological analysis for stress detection. The system provides a scalable and wearable-friendly approach for non-invasive stress monitoring and lays the groundwork for future real-time healthcare applications.

---

## Author
**Laashya Lakshmi M**  

