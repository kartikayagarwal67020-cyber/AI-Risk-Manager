# 🛡️ AI Risk Manager

### AI-Powered Payment Risk & Fraud Detection System

> **Razorpay Buildathon – AI Risk Management Track**

AI Risk Manager is an AI/ML-powered payment risk management platform that analyzes transaction data, estimates fraud probability, generates a **0–100 risk score**, classifies transactions by risk level, and provides explainable alerts for suspicious activity.

## 🎯 Problem Statement

Digital payments are growing rapidly, but payment fraud remains a major challenge. Traditional rule-based systems may miss evolving fraud patterns, while excessive alerts can affect genuine customers.

The goal is to build an intelligent risk management layer that can quickly identify suspicious payment behavior and support better transaction decisions.

## 💡 Our Solution

AI Risk Manager uses a **Random Forest Classifier** to analyze transaction features and estimate the probability of fraud.

The system then converts the model output into an easy-to-understand risk score:

- 🟢 **LOW RISK:** 0–29
- 🟠 **MEDIUM RISK:** 30–69
- 🔴 **HIGH RISK:** 70–100

For suspicious transactions, the application also provides risk explanations and alerts.

## ✨ Key Features

- 🤖 AI-based payment fraud detection
- 📊 Real-time risk score from 0–100
- 🔴 High / 🟠 Medium / 🟢 Low risk classification
- 🚨 High-risk fraud alerts
- 💡 Explainable risk reasons
- 📈 Interactive risk monitoring dashboard
- 🤖 AI prediction history
- 🔎 Transaction analysis
- 📊 Model performance monitoring
- 🔄 Automatic dashboard refresh

## 🔗 Razorpay / Payment Ecosystem Relevance

The system is designed as an **AI risk-management layer for a digital payment ecosystem**.

In a production payment flow, the architecture can be connected to a payment platform such as Razorpay so that transaction information can be evaluated by the risk engine before or during payment processing.

### Proposed Flow

```text
Customer Payment
       ↓
Payment Platform / Razorpay
       ↓
AI Risk Manager
       ↓
Transaction Feature Analysis
       ↓
Random Forest Model
       ↓
Fraud Probability
       ↓
Risk Score (0–100)
       ↓
┌──────────────┬───────────────┬──────────────┐
│   LOW RISK   │  MEDIUM RISK  │  HIGH RISK   │
│   Proceed    │   Verify      │   Review /   │
│              │               │   Block*     │
└──────────────┴───────────────┴──────────────┘
```

`* Blocking is a proposed production action; the current prototype demonstrates risk detection and alerts rather than live transaction blocking.`

## 🧠 Machine Learning Model

### Model Used
**Random Forest Classifier**

The model is trained using the **Credit Card Fraud Detection** dataset.

### Dataset

- Total transactions: **284,807**
- Fraud transactions: **492**
- Safe transactions: **284,315**
- Fraud rate: approximately **0.17%**

The dataset is highly imbalanced, so accuracy alone is not sufficient for evaluating fraud detection performance.

### Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 99.95% |
| Precision | 90.59% |
| Recall | 78.57% |
| F1 Score | 84.15% |

## ⚙️ How It Works

1. User enters a transaction ID.
2. The application retrieves the corresponding transaction data.
3. The Random Forest model predicts the transaction class.
4. The model calculates fraud probability.
5. Probability is converted into a **0–100 risk score**.
6. The system assigns Low, Medium, or High Risk.
7. Explainable reasons and alerts are displayed.
8. The result is stored in prediction history.
9. The dashboard provides an overview of analyzed transactions.

## 🖥️ Application Modules

### 1. Risk Analyzer
Analyzes an individual transaction and displays:

- Risk level
- Risk score
- Fraud probability
- Transaction amount
- Risk explanation
- Security alert

### 2. Risk Dashboard
Provides:

- Total transaction statistics
- Fraud/safe transaction counts
- Fraud rate
- Risk summary
- AI model performance
- High-risk transaction list
- Prediction history

## 🛠️ Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Random Forest
- Pandas
- NumPy
- Joblib

### Deployment / Cloud Direction
- AWS (planned production deployment)

## 📁 Project Structure

```text
AI_RISK_MANAGER/
│
├── app.py
├── train_model.py
├── risk_model.pkl
├── README.md
│
└── templates/
    ├── index.html
    └── dashboard.html
```

### Dataset Note

The original `creditcard.csv` dataset is used for model training. Due to repository-size considerations, it is recommended to keep large dataset files out of the public Git repository and document the dataset source separately.

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Risk-Manager.git
cd AI-Risk-Manager
```

### 2. Install Dependencies

```bash
pip install pandas numpy scikit-learn flask joblib
```

### 3. Train the Model

If `risk_model.pkl` is not available:

```bash
python train_model.py
```

This generates the trained model file:

```text
risk_model.pkl
```

### 4. Start the Application

```bash
python app.py
```

### 5. Open the Application

```text
http://127.0.0.1:5000
```

Dashboard:

```text
http://127.0.0.1:5000/dashboard
```

## 🧪 Demo

Example transactions tested with the trained model:

| Transaction ID | Result |
|---:|---|
| 4920 | 🔴 HIGH RISK |
| 6108 | 🔴 HIGH RISK |
| 0 | 🟢 LOW RISK |

For the demo, the application shows the risk score, fraud probability, alert, and explanation.

## 🌟 Innovation / USP

### 1. Risk Score Instead of Only Fraud/Not-Fraud
A 0–100 score makes the model output easier to interpret.

### 2. Explainable Risk Alerts
The system provides understandable reasons for a risk decision.

### 3. Three-Level Risk Classification
Low, Medium, and High Risk can support different payment decisions.

### 4. Real-Time Monitoring Dashboard
Risk information can be viewed from a single dashboard.

### 5. Prediction History
Previous AI predictions can be monitored for analysis.

## 🔮 Future Scope

- Live payment-platform integration
- Real-time transaction streaming
- Razorpay-compatible payment workflow integration
- XGBoost and deep-learning models
- SHAP/LIME explainable AI
- Device and behavioral analysis
- IP/geolocation-based risk signals
- Automated transaction blocking
- Email/SMS security alerts
- AWS cloud deployment
- Model monitoring and retraining

## 👥 Team

**Project:** AI Risk Manager  
**Track:** AI Risk Management

## 📌 Disclaimer

This project is a hackathon prototype for demonstrating AI-based payment risk detection. It is not intended to make real financial decisions without appropriate production-grade security, compliance, monitoring, testing, and payment-platform integration.

---

⭐ If you find this project useful, consider giving the repository a star.
