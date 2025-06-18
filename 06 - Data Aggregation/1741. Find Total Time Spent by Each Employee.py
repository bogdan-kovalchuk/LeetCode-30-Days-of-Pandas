import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    employees = employees.rename(columns={"event_day": "day"})
    employees = employees.drop(["in_time", "out_time"], axis=1)
    return employees.groupby(by=["day", "emp_id"], as_index=False)["total_time"].sum()
