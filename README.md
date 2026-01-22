## 📊 Business Problem

Customer churn is a major challenge in the telecommunications industry, where customer acquisition costs are high and competition is intense.

This project focuses on predicting customer churn using machine learning techniques. By identifying customers who are likely to leave, businesses can take proactive measures such as targeted promotions, personalized offers, or service improvements to retain valuable customers.

The model prioritizes minimizing false negatives, as failing to identify a churn-risk customer results in lost revenue and missed retention opportunities.

---

# ❓ What is Churn?

Churn occurs when a customer terminates their relationship with a company.
In this dataset, churn is represented as a binary variable:

- Yes → Customer has left the company

- No → Customer is still an active customer

---

# ❓ Why Does Churn Matter?

Customer churn directly impacts:

- Revenue loss

- Customer lifetime value

- Marketing and acquisition costs

Reducing churn by even a small percentage can lead to significant increases in profit.
Therefore, predicting churn accurately is a high-value business problem.

---

# ❓ What Happens If We Predict Wrong?

| Scenario                                                    | Impact                                         |
| ----------------------------------------------------------- | ---------------------------------------------- |
| **False Negative** (predict “No churn” but customer leaves) | Lost revenue, missed retention opportunity     |
| **False Positive** (predict “Churn” but customer stays)     | Unnecessary discounts or incentives            |
| **Correct Prediction**                                      | Targeted actions, optimized retention strategy |

From a business perspective, false negatives are more costly, as losing a customer is harder to recover than offering an unnecessary incentive.

---

# 🎯 Business Objective

The goal of this project is to:

_Predict customer churn with high recall_

_Identify key factors influencing churn_

_Provide actionable insights to reduce customer attrition_

---

### ⚠️ Model Limitations

While Random Forest provides strong performance, it is less interpretable than Logistic Regression. Feature importance was analyzed to partially mitigate this limitation.

---

## Keywords:

- EDA == Exploratory Data Analysis
