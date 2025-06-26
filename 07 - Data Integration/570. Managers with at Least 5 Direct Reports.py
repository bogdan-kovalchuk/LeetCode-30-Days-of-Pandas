import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers_id_count = employee["managerId"].value_counts().reset_index()
    filtered_managers_id = managers_id_count[managers_id_count["count"] >= 5]
    return employee[employee["id"].isin(filtered_managers_id["managerId"])][["name"]]
