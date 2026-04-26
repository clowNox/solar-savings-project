# Solar Lead Scoring Engine: A B2C Machine Learning Case Study

Customer acquisition in the solar industry is notoriously expensive. Sales teams waste countless hours pitching to households where solar simply isn't financially viable due to small house sizes, low energy consumption, or poor subsidy applicability.

This project is a **Machine Learning pipeline designed to automatically score and qualify solar leads**. By predicting a household's Return on Investment (ROI) and Payback Period, sales teams can instantly separate highly profitable "Hot Leads" from low-value "Cold Leads" before picking up the phone.

> 📖 **Read the Full Business Case Study:** Check out the [B2C_CASE_STUDY.md](B2C_CASE_STUDY.md) for a deep dive into the business impact, data pipeline, and predictive models.

## ⚙️ The ML Engine

This repository combines exploratory predictive modeling with business-focused classifiers:

1. **The Lead Qualifier (High ROI Classifier)**: An ML model (Accuracy: 89%, ROC AUC: 0.91) that instantly flags whether a specific household will see a "High ROI" from a solar installation. 
2. **The Value Prop Generator (Regression Models)**: Models (Random Forest, XGBoost) that predict the exact *Monthly Savings (₹)* and *Payback Period* for a household. This data can be automatically injected into a sales pitch.

## 📂 Project Structure

### 1. Modular ML Pipeline (Sync-Ready)
This project is structured like a production-grade software application, allowing the dashboard/frontend to "sync" with the pre-trained models.
- **`train.py`**: Ingests household data, applies a PCA pipeline for noise reduction, trains the models, and serializes them to the `models/` directory.
- **`predict.py`**: A deployment script that instantly loads the `.joblib` model and scores new leads in milliseconds without needing to retrain.
- **`models/`**: Stores the serialized `.joblib` model files.
- **`requirements.txt`**: Strict dependency locks to ensure the environment syncs perfectly across machines.

### 2. Exploratory Notebooks
- **`solar_analysis.ipynb`**: The core ML pipeline where the ROI Classifier and Payback regressions are trained.
- **`Solar_mini.ipynb`**: An exploratory notebook analyzing the specific relationships between Indian government subsidies, household size, and grid metrics to predict the final post-solar electricity bill.
- **`solar_dashboard_full.ipynb`**: An interactive dashboard simulation. A sales rep can plug in a prospect's data here and instantly receive their "Lead Score" and financial projections.
- **`solar_project_compact.ipynb`**: A streamlined, production-ready version of the analysis.

## 💻 Running Locally

To run the modular pipeline:
1. **Install dependencies:** `pip install -r requirements.txt`
2. **Train & Sync the model:** `python train.py` (This will output `high_roi_classifier.joblib` to the `models/` directory).
3. **Score a new Lead:** `python predict.py`

## 🚀 Impact

By implementing this ML pipeline, solar installation companies can:
- **Decrease Customer Acquisition Cost (CAC)** by stopping ad spend on households predicted to have poor solar ROI.
- **Increase Sales Conversion Rates** by empowering sales reps with personalized, data-backed financial projections for every lead.
