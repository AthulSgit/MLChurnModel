# Telco Customer Churn Prediction

This project is an end-to-end machine learning system that predicts customer churn using an XGBoost model. It includes data preprocessing, feature engineering, model training, and deployment using FastAPI with a Gradio interface.

## Tech Stack
Python, pandas, scikit-learn, XGBoost, MLflow (experiment tracking only), FastAPI, Gradio, Uvicorn

## Workflow
Raw Data -> Preprocessing -> Feature Engineering -> Model Training -> MLflow Logging -> Model Saving (joblib) -> FastAPI Inference -> Gradio UI

## How to Run

Install dependencies:
pip install -r requirements.txt

Train model:
python scripts/run_pipeline.py --input data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv

Run application:
uvicorn src.app.main:app --reload

## Access
API: http://127.0.0.1:8000  
UI: http://127.0.0.1:8000/ui

## Screenshot
<img width="1240" height="1944" alt="Screenshot_30-4-2026_211339_127 0 0 1" src="https://github.com/user-attachments/assets/1a497dc3-eaa7-40b0-be2e-acd497f033ba" />

## Note
MLflow is used only for experiment tracking. Model serving is done using the saved joblib model.
