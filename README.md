# 💰 Loan Risk Analyzer

A Machine Learning-based web application that predicts whether a loan applicant is at **Low Risk** or **High Risk** using financial information. The application is built using **Python, Flask, Scikit-learn, HTML, CSS, and JavaScript**, and includes PDF report generation and prediction history tracking.

---

## 📌 Project Overview

The Loan Risk Analyzer helps financial institutions evaluate loan applications by predicting the applicant's risk level. Users enter applicant details such as income, loan amount, credit score, and age. The trained Random Forest model analyzes the information and classifies the applicant as either **Low Risk** or **High Risk**.

The application also stores prediction history and allows users to download a PDF report of the latest prediction. The Flask application loads the dataset, trains a Random Forest classifier, processes prediction requests, saves prediction history, and generates PDF reports. :contentReference[oaicite:0]{index=0}

---

## 🎯 Objectives

- Predict loan risk using Machine Learning.
- Assist banks in making faster loan approval decisions.
- Reduce manual loan evaluation.
- Maintain prediction history.
- Generate downloadable loan analysis reports.

---

## ✨ Features

- User-friendly dashboard
- Loan risk prediction
- Real-time analysis
- Prediction probability
- Loan approval/rejection decision
- Prediction history
- PDF report generation
- Responsive web interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- Random Forest Classifier

### Report Generation
- ReportLab

### Data Storage
- JSON (Prediction History)

---

## 📂 Project Structure

```
Loan-Risk-Analyzer/
│
├── app.py
├── train_model.py
├── model.pkl
├── loan_data.csv
├── history.json
├── templates/
│   ├── dashboard.html
│   ├── predict.html
│   ├── result.html
│   └── history.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

## 📊 Input Parameters

The application accepts the following user inputs:

- Name
- Gender
- Age
- Annual Income
- Loan Amount
- Credit Score

---

## 🔄 Project Workflow

```
Start
   │
   ▼
Open Dashboard
   │
   ▼
Enter Applicant Details
   │
   ▼
Submit Application
   │
   ▼
Machine Learning Prediction
   │
   ▼
Risk Analysis
   │
   ▼
Display Result
   │
   ▼
Save Prediction History
   │
   ▼
Generate PDF Report
   │
   ▼
End
```

---

## 🤖 Machine Learning Workflow

1. Load the loan dataset.
2. Separate input features and target.
3. Train a Random Forest Classifier.
4. Predict applicant risk.
5. Calculate prediction probability.
6. Display loan decision.

The model is trained using the loan dataset with a Random Forest classifier before being saved for use in predictions. :contentReference[oaicite:1]{index=1}

---

## 📈 Prediction Output

The application displays:

- Applicant Name
- Income
- Loan Amount
- Credit Score
- Risk Status
- Prediction Probability
- Loan Decision (Approved / Rejected)

---

## 📑 History Module

Every prediction is automatically stored with:

- Applicant Name
- Income
- Loan Amount
- Risk Level
- Prediction Probability
- Date & Time

Users can view previous loan analyses through the History page. :contentReference[oaicite:2]{index=2}

---

## 📄 PDF Report

The application can generate a PDF report containing:

- Applicant Name
- Income
- Loan Amount
- Risk Status
- Prediction Probability

The PDF is automatically downloaded when requested. :contentReference[oaicite:3]{index=3}

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Loan-Risk-Analyzer.git
```

### Navigate to the Project Folder

```bash
cd Loan-Risk-Analyzer
```

### Install Dependencies

```bash
pip install flask pandas scikit-learn reportlab
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📦 Required Libraries

- Flask
- Pandas
- Scikit-learn
- ReportLab
- NumPy

---

## 🎯 Advantages

- Fast loan risk prediction
- Easy to use
- Automated decision support
- Stores prediction history
- Generates PDF reports
- Reduces manual effort

---

## 🔮 Future Enhancements

- User Authentication
- Admin Dashboard
- Database Integration (MySQL)
- Explainable AI (XAI)
- Email Notifications
- Cloud Deployment
- Credit Score API Integration
- Advanced Risk Analytics

---
