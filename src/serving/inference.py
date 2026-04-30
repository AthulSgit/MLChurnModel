import os
import pandas as pd
import joblib

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

MODEL_PATH = os.path.join(PROJECT_ROOT, "artifacts", "xgb_model.pkl")
FEATURE_FILE = os.path.join(PROJECT_ROOT, "artifacts", "feature_columns.json")

# load model
model = joblib.load(MODEL_PATH)

# load features
import json
with open(FEATURE_FILE, "r") as f:
    FEATURE_COLS = json.load(f)

BINARY_MAP = {
    "gender": {"Female": 0, "Male": 1},
    "Partner": {"No": 0, "Yes": 1},
    "Dependents": {"No": 0, "Yes": 1},
    "PhoneService": {"No": 0, "Yes": 1},
    "PaperlessBilling": {"No": 0, "Yes": 1},
}

NUMERIC_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]


def _transform(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    for c in NUMERIC_COLS:
        if c in df:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

    for c, m in BINARY_MAP.items():
        if c in df:
            df[c] = df[c].astype(str).str.strip().map(m).fillna(0).astype(int)

    obj_cols = df.select_dtypes(include=["object"]).columns
    df = pd.get_dummies(df, columns=obj_cols, drop_first=True)

    df = df.reindex(columns=FEATURE_COLS, fill_value=0)

    return df


def predict(input_dict):
    df = pd.DataFrame([input_dict])
    X = _transform(df)

    pred = model.predict(X)[0]

    return "Likely to churn" if pred == 1 else "Not likely to churn"