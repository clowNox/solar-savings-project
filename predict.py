import joblib
import pandas as pd
import sys

def load_model():
    """
    Loads the serialized model from the models/ directory.
    This demonstrates how the dashboard can "sync" without retraining.
    """
    try:
        model = joblib.load('models/high_roi_classifier.joblib')
        return model
    except FileNotFoundError:
        print("Error: Model not found. Please run train.py first to generate the .joblib file.")
        sys.exit(1)

def score_lead(household_data):
    """
    Takes a dictionary of household data, converts to DataFrame, and scores it.
    """
    model = load_model()
    
    # Ensure correct feature order
    features = [
        'Household_Size', 'House_Area_sqft', 'Monthly_Consumption_kWh',
        'Solar_Setup_Cost', 'Govt_Solar_Subsidy_%', 'Net_Metering_Credit_per_kWh',
        'Average_Sunlight_Hours'
    ]
    
    df = pd.DataFrame([household_data], columns=features)
    
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    
    result = "High ROI (HOT LEAD)" if prediction == 1 else "Low ROI (COLD LEAD)"
    
    return {
        "Status": result,
        "Confidence_Score": f"{probability:.2%}"
    }

if __name__ == "__main__":
    # Example Dashboard Sync Input
    sample_prospect = {
        'Household_Size': 4,
        'House_Area_sqft': 2500,
        'Monthly_Consumption_kWh': 850,
        'Solar_Setup_Cost': 250000,
        'Govt_Solar_Subsidy_%': 40,
        'Net_Metering_Credit_per_kWh': 4.5,
        'Average_Sunlight_Hours': 6.2  # Our new CS229-inspired weather feature
    }
    
    print("Syncing with ML Backend...")
    print("Scoring Prospect Data:", sample_prospect)
    
    score = score_lead(sample_prospect)
    
    print("\n--- LEAD SCORING RESULT ---")
    print(f"Lead Classification: {score['Status']}")
    print(f"AI Confidence: {score['Confidence_Score']}")
