import pandas as pd
import numpy as np


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [np.nan]})

    salaries = employee["salary"].drop_duplicates().nlargest(N)
    nth_salary = salaries.iloc[-1] if len(salaries) == N else np.nan
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_salary]})
