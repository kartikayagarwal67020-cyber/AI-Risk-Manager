from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
prediction_history=[]

# Load model and dataset
model = joblib.load("risk_model.pkl")
df = pd.read_csv("creditcard.csv")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Dashboard
@app.route("/dashboard")
def dashboard():

    total = len(df)

    fraud = int(df["Class"].sum())


    safe = total - fraud

    fraud_rate = round((fraud / total) * 100, 2)
    safe_rate = round((safe / total) * 100, 2)

    recent = df.tail(10).copy()

    recent["Transaction_ID"] = recent.index

    transactions = recent[
        ["Transaction_ID", "Amount", "Class"]
    ].to_dict("records")

    return render_template(
        "dashboard.html",
        total=total,
        fraud=fraud,
        safe=safe,
        safe_rate=safe_rate,
        fraud_rate=fraud_rate,
        transactions=transactions,
        prediction_history=prediction_history
    )


# Risk Prediction
@app.route("/predict", methods=["POST"])
def predict():

    transaction_id = int(request.form["transaction_id"])

    transaction = df.iloc[[transaction_id]]

    X = transaction.drop("Class", axis=1)

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0][1]

    risk_score = round(probability * 100)

    if risk_score >= 70:
        risk = "HIGH RISK"
        risk_class = "risk-high"
    elif risk_score >= 30:
        risk = "MEDIUM RISK"
        risk_class = "risk-medium"
    else:
        risk = "LOW RISK"
        risk_class = "risk-low"

    reasons = []

    amount = float(transaction["Amount"].iloc[0])
    time = float(transaction["Time"].iloc[0])

    if amount > 1000:
        reasons.append("💰 High transaction amount")
    elif amount > 500:
        reasons.append("💰 Moderately high transaction amount")

    if prediction == 1:
        reasons.append("🤖 AI model detected a suspicious transaction pattern")

    if risk_score >= 70:
        reasons.append("🚨 Very high fraud probability")
    elif risk_score >= 30:
        reasons.append("⚠️ Moderate fraud probability")
    else:
        reasons.append("✅ Low fraud probability")

    if time < 1000:
        reasons.append("🕐 Transaction occurred during an early recorded period")

    # Save prediction history
    prediction_history.append({
        "transaction_id": transaction_id,
        "amount": round(amount, 2),
        "risk_score": risk_score,
        "probability": round(probability * 100, 2),
        "risk": risk
    })

    # Keep latest 20 predictions
    if len(prediction_history) > 20:
        del prediction_history[:-20]

    # Return result
    return render_template(
        "index.html",
        risk=risk,
        risk_class=risk_class,
        score=risk_score,
        probability=round(probability * 100, 2),
        reasons=reasons,
        amount=round(amount, 2),
        transaction_id=transaction_id,
        time=round(time, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)