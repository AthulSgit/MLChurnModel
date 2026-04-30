from typing import Tuple, List

def validate_telco_data(df) -> Tuple[bool, List[str]]:
    print("Starting lightweight data validation...")

    failed = []

    required_columns = [
        "customerID",
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "InternetService",
        "Contract",
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    # Check required columns
    for col in required_columns:
        if col not in df.columns:
            failed.append(f"Missing column: {col}")

    # Null checks
    for col in ["customerID", "tenure", "MonthlyCharges"]:
        if df[col].isna().sum() > 0:
            failed.append(f"Null values in {col}")

    # Allowed categorical values
    if not df["gender"].isin(["Male", "Female"]).all():
        failed.append("Invalid gender values")

    if not df["Partner"].isin(["Yes", "No"]).all():
        failed.append("Invalid Partner values")

    # Numeric checks
    if (df["tenure"] < 0).any():
        failed.append("Negative tenure values")

    if (df["MonthlyCharges"] < 0).any():
        failed.append("Negative MonthlyCharges values")

    is_valid = len(failed) == 0

    if is_valid:
        print("Data validation PASSED")
    else:
        print("Data validation FAILED")
        print(failed)

    return is_valid, failed