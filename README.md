# 📄 Customer Churn Prediction (Machine Learning)

## 📌 Project Overview

Customer churn is a critical business problem where companies lose customers to competitors. This project builds an **end-to-end machine learning pipeline** to predict customer churn and help businesses take **proactive retention actions**.

The solution covers the full ML lifecycle:

- Business understanding
- Data analysis & preprocessing
- Model training & tuning
- Model selection
- Deployment-ready model saving

---

## 🎯 Business Problem

**Goal:** Predict whether a customer is likely to churn.

**Why it matters:**

- Retaining existing customers is cheaper than acquiring new ones
- Early churn detection enables targeted retention strategies

**Cost of errors:**

- False Negative (missed churner): Customer leaves → revenue loss
- False Positive: Retention offer cost (acceptable)

📌 **Recall is prioritized** over accuracy.

---

## 📊 Dataset

- **Source:** Telco Customer Churn Dataset (Kaggle)
- **Size:** ~7,000 customers
- **Target Variable:** `Churn`
- **Features:** Demographics, services, contract, and billing information

---

## 🔍 Exploratory Data Analysis (EDA)

Key insights:

- Month-to-month contracts show higher churn
- Higher monthly charges correlate with churn
- Longer tenure reduces churn probability

---

## 🧹 Data Preprocessing

Steps performed:

- Data cleaning and type correction
- Encoding categorical variables
- Handling class imbalance
- Feature consistency checks

Processed data saved to:

```
data/processed/clean_telco_churn.csv
```

---

## 🤖 Models Trained

- Logistic Regression
- Decision Tree
- Random Forest
- Random Forest (Tuned)
- XGBoost (experimental)

---

## ⚙️ Model Evaluation

Metrics used:

- Recall (primary)
- ROC-AUC
- Precision
- F1-score

---

## 🏆 Final Model Selection

### ✅ Tuned Random Forest

**Reasons:**

- Highest recall
- Strong ROC-AUC
- Reduced overfitting after tuning
- Balanced performance and interpretability

---

## 💾 Deployment Readiness

The final model was retrained on the full dataset and saved using `joblib`.

Artifacts:

```
models/
├── churn_random_forest_model.pkl
└── model_metadata.pkl
```

---

## 📁 Project Structure

```
churn-prediction-ml/
├── data/
├── notebooks/
├── models/
├── results/
└── README.md
```

---

## 🚀 Future Improvements

- SHAP explainability
- FastAPI deployment
- Automated retraining

---

## 🧠 Skills Demonstrated

- Business-focused ML
- Model tuning & evaluation
- Experiment tracking
- Deployment preparation

---

## 📬 Contact

**Name:** Hoda Al Hashash  
**Field:** Machine Learning / Data Science  
**Goal:** AI Researcher / ML Engineer
