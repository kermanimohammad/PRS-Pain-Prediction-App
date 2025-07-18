# PRS & Pain Prediction App

This is an interactive web app built with **Streamlit** that predicts:

- **Polygenic Risk Score (PRS)** using a trained regression model  
- **Pain presence (yes/no)** using a trained classification model  

It uses four cluster-based features (`C1`, `C2`, `C3`, `C4`) as inputs.

---

## 🚀 Live Demo

👉 [Try the app on Streamlit Cloud](https://prs-pain-prediction-app.streamlit.app/)  
*(Replace with your actual Streamlit app URL after deployment)*

---

## 🧠 How It Works

1. Enter values for `C1`, `C2`, `C3`, and `C4`
2. Click the **Predict** button
3. The app will display:
   - Predicted **PRS** value
   - Predicted **Pain** status

---

## 📁 Project Structure

predict_app/
├── predict_app.py # Streamlit app
├── prs_predictor.pkl # Trained regression model
├── pain_classifier.pkl # Trained classification model
├── requirements.txt # Python dependencies


## 💻 Run Locally

### 1. Clone this repo:

git clone https://github.com/kermanimohammad/PRS-Pain-Prediction-App.git

cd prs-pain-predictor

### 2. Install dependencies:

pip install -r requirements.txt

### 3. Launch the app:

**streamlit run predict_app.py**

🧪 Requirements:
• Python 3.7+
• streamlit
• scikit-learn
• joblib
• numpy

👨‍🔬 Author
Mohammad Mehdi Kermani
• [LinkedIn](https://www.linkedin.com/in/mohamadkermani/) 
• [GitHub](https://github.com/kermanimohammad/)

