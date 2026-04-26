import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import os

# Ensure models directory exists
os.makedirs('models', exist_ok=True)

def generate_mock_data(n_samples=1000):
    """
    Generate mock dataset since the original CSV isn't checked in.
    Incorporates CS229-inspired weather features (Average_Sunlight_Hours)
    """
    np.random.seed(42)
    return pd.DataFrame({
        'Household_Size': np.random.randint(1, 8, n_samples),
        'House_Area_sqft': np.random.randint(500, 4000, n_samples),
        'Monthly_Consumption_kWh': np.random.uniform(200, 1500, n_samples),
        'Solar_Setup_Cost': np.random.uniform(100000, 500000, n_samples),
        'Govt_Solar_Subsidy_%': np.random.choice([0, 20, 40], n_samples),
        'Net_Metering_Credit_per_kWh': np.random.uniform(2, 6, n_samples),
        'Average_Sunlight_Hours': np.random.uniform(4, 8, n_samples), # Weather inspired feature
        'High_ROI': np.random.choice([0, 1], n_samples, p=[0.3, 0.7]) # Target Variable
    })

def train_and_save_model():
    print("Loading data...")
    df = generate_mock_data()
    
    X = df.drop('High_ROI', axis=1)
    y = df['High_ROI']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Building ML Pipeline with PCA...")
    # Using PCA to reduce noise, inspired by Stanford CS229 project
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=5)),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    print("Training model...")
    pipeline.fit(X_train, y_train)
    
    score = pipeline.score(X_test, y_test)
    print(f"Model trained successfully. Accuracy: {score:.2f}")
    
    print("Exporting model to models/ directory...")
    joblib.dump(pipeline, 'models/high_roi_classifier.joblib')
    print("Model saved to models/high_roi_classifier.joblib. Ready for Dashboard Sync!")

if __name__ == "__main__":
    train_and_save_model()
