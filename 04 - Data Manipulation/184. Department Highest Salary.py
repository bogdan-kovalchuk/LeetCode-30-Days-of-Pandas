import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on="departmentId", right_on="id")
    merged["max_salary"] = merged.groupby("departmentId")["salary"].transform("max")
    top_earners = merged[merged["salary"] == merged["max_salary"]]
    return top_earners[["name_y", "name_x", "salary"]].rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
