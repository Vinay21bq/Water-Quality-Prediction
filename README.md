# 💧 Water Quality Prediction App (CNN-LSTM)

This project is a deep learning-based web application that predicts water quality using a hybrid CNN-LSTM model. It analyzes important water parameters like temperature, pH, dissolved oxygen, and others to determine whether the water is suitable for drinking.

---

## 🚀 Features

- 🧠 Hybrid Deep Learning: Combines CNN and LSTM for improved prediction accuracy
- 🌐 Web Interface: Built using Streamlit for user-friendly input and instant prediction
- 📊 Input Parameters: 
  - Temperature
  - Dissolved Oxygen (D.O)
  - pH
  - Conductivity
  - Biochemical Oxygen Demand (B.O.D)
  - Nitrate
  - Fecal Caliform
  - Total Caliform
- ✅ Output: Whether the water is **suitable for drinking** or **not**

---
## 🛠️ Installation & Running Locally

### 🔧 Prerequisites
- Python 3.10 or 3.11 recommended
- pip installed
- Git installed (optional)

### 📦 Install Requirements

```bash
pip install streamlit tensorflow numpy scikit-learn
streamlit run app.py
