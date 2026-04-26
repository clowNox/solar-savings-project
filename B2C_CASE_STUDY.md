# Business Case Study: AI-Powered Solar Lead Scoring

## Executive Summary

Customer acquisition is one of the highest operational costs for solar installation companies. A typical solar sales team purchases thousands of localized leads and spends countless hours cold-calling and pitching to households. 

The core business problem? **Not every household is a financially viable candidate for solar energy.** 

Factors like small roof square footage, low monthly energy consumption, and localized subsidy limits can mean that a household's "Payback Period" stretches beyond 10+ years. When sales reps unknowingly pitch to these households, the conversion rate plummets and valuable operational hours are wasted.

This project introduces a **Machine Learning Lead Scoring Engine**. By analyzing household data against local energy metrics, the engine instantly qualifies leads—allowing sales teams to focus 100% of their energy on high-probability "Hot Leads."

---

## The Data Pipeline

The engine evaluates leads based on a localized feature set, including:
- **Household Info:** `Household_Size`, `House_Area_sqft`
- **Current Energy Usage:** `Monthly_Consumption_kWh`
- **Cost & Policy Variables:** `Solar_Setup_Cost`, `Govt_Solar_Subsidy_%`, `Net_Metering_Credit_per_kWh`

These data points act as the inputs for our scoring engine.

---

## The ML Engine

The solution is divided into two distinct machine learning pipelines: The Qualifier and The Value Prop Generator.

### 1. The Lead Qualifier (High ROI Classifier)
Instead of just predicting a raw financial number, we built a classification model specifically tuned for sales teams. 

- **How it works:** It takes the household data and classifies the lead as either a "Good Investment" (High ROI) or a "Poor Investment."
- **Performance:** Achieved an **89% Accuracy** and a **0.91 ROC AUC**.
- **Business Application:** This acts as the gatekeeper. Leads flagged as "Poor Investments" are automatically filtered out of the CRM or deprioritized, saving the sales team from making dead-end calls.

### 2. The Value Prop Generator (Regression Models)
Once a lead is qualified as a "Hot Lead," the sales rep needs a compelling pitch. 

- **How it works:** We utilized ensemble regression models (Random Forest, XGBoost) to predict the exact **Monthly Savings (₹)** and the **Payback Period** (in years).
- **Performance:** The ROI model achieved an **R² Score of 0.79**, meaning it is highly reliable at tracking the variance in actual return on investment.
- **Business Application:** A sales rep can call the "Hot Lead" and immediately say: *"Based on your 1500 sqft house and local 40% government subsidy, our models predict you will save exactly ₹2,500 a month and your setup will pay for itself in just 4.2 years."*

---

## Business Impact & ROI

Implementing this ML pipeline into a solar company's CRM fundamentally shifts their unit economics:

1. **Decreased Customer Acquisition Cost (CAC):** By immediately disqualifying households that don't make financial sense, marketing teams can adjust ad targeting, and sales teams stop wasting hours on un-convertible leads.
2. **Increased Sales Conversion:** Cold outreach is transformed into highly personalized financial consulting. Sales reps are armed with hyper-accurate, data-backed financial projections tailored exactly to the prospect's household size and local subsidies.
3. **Data-Driven Operations:** The `solar_dashboard_full.ipynb` provides management with a clear, interactive view of the financial viability of different territories, allowing for strategic expansion planning.
