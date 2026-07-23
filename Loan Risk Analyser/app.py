from flask import Flask, render_template, request, send_file
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import json
import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

HISTORY_FILE = "history.json"

# =========================
# LOAD DATASET & TRAIN MODEL
# =========================
data = pd.read_csv("loan_data.csv")

X = data.drop("target", axis=1)
y = data["target"]

model = RandomForestClassifier()
model.fit(X, y)

# =========================
# HISTORY FUNCTIONS
# =========================
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/analyse", methods=["POST"])
def analyse():

    data_form = request.form

    features = [
        float(data_form["income"]),
        float(data_form["loan_amount"]),
        float(data_form["credit_score"]),
        float(data_form["age"])
    ]

    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1] * 100

    result = "High Risk" if prediction == 1 else "Low Risk"

    # SAVE HISTORY
    history = load_history()
    record = {
        "name": data_form["name"],
        "income": data_form["income"],
        "loan": data_form["loan_amount"],
        "risk": result,
        "probability": round(probability, 2),
        "time": str(datetime.now())
    }
    history.append(record)
    save_history(history)

    return render_template(
        "result.html",
        name=data_form["name"],
        age=data_form["age"],
        gender=data_form["gender"],
        income=data_form["income"],
        loan=data_form["loan_amount"],
        score=data_form["credit_score"],
        risk=result,
        probability=round(probability, 2),
        decision="Approved" if result == "Low Risk" else "Rejected"
    )


# =========================
# PDF DOWNLOAD
# =========================
@app.route("/download")
def download():

    history = load_history()
    last = history[-1]

    file_path = "loan_report.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = [
        Paragraph("Loan Risk Analysis Report", styles["Title"]),
        Spacer(1, 12),

        Paragraph(f"Name: {last['name']}", styles["Normal"]),
        Paragraph(f"Income: {last['income']}", styles["Normal"]),
        Paragraph(f"Loan: {last['loan']}", styles["Normal"]),
        Paragraph(f"Risk: {last['risk']}", styles["Normal"]),
        Paragraph(f"Probability: {last['probability']}%", styles["Normal"])
    ]

    doc.build(content)

    return send_file(file_path, as_attachment=True)


# =========================
# HISTORY PAGE
# =========================
@app.route("/history")
def history():

    data = load_history()
    return render_template("history.html", history=data)


if __name__ == "__main__":
    app.run(debug=True)