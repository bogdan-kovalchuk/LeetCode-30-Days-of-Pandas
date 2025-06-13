import pandas as pd
import numpy as np


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee["salary"].drop_duplicates().nlargest(2)
    second = salaries.iloc[1] if len(salaries) == 2 else np.nan
    return pd.DataFrame({"SecondHighestSalary": [second]})
