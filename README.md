# 🧪 A/B Test: In-App Purchase Pricing Strategy

This project simulates and analyzes an A/B test to evaluate the impact of introducing a low-priced ($1) starter pack in a mobile game. The goal is to determine whether this pricing change improves user monetization and retention.

---

## 🎯 Objective

To test whether adding a $1 “starter pack” increases:
- **ARPU** (Average Revenue Per User)
- **Conversion Rate**
- and reduces **Churn Rate**

---

## 📦 Test Design

| Group | Offer Details                                  |
|-------|------------------------------------------------|
| A     | 3-pack (5, 10, 20 USD) – original setup         |
| B     | 3-pack + $1 starter pack – modified pricing     |

Each group consists of **4,347 simulated users**.

---

## 📊 Key Metrics

- **Conversion Rate** – % of users who made a purchase  
- **ARPU** – Total revenue divided by number of users  
- **Churn Rate** – % of users who stopped playing

---

## 📈 Results Summary

| Metric            | Group A     | Group B     |
|-------------------|-------------|-------------|
| Conversion Rate   | 9.57%       | 15.11%      |
| ARPU              | $0.074      | $0.136      |
| Churn Rate        | 33.1%       | 32.0%       |
| Welch's t-test (ARPU) | p < 0.001 | ✅ Significant |
| Z-test (Churn)    | p = 0.27    | ❌ Not Significant |
| Cohen's d (ARPU)  | -0.189      | Small Effect |

---

## 🧪 Statistical Methods

- Welch’s t-test for ARPU comparison  
- Z-test for churn rate comparison  
- 95% Confidence Intervals  
- Cohen’s d for effect size  
- Visualizations: histograms, bar plots, box plots

---
