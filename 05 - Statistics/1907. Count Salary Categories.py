import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = (accounts["income"] < 20000).sum()
    average = ((accounts["income"] >= 20000) & (accounts["income"] <= 50000)).sum()
    high = (accounts["income"] > 50000).sum()

    return pd.DataFrame({"category": ["Low Salary", "Average Salary", "High Salary"], "accounts_count": [low, average, high]}) 
