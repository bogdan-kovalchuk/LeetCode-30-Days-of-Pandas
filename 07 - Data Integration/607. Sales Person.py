import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    com_id = company[company["name"] == "RED"]["com_id"]
    sales_ids = orders[orders["com_id"].isin(com_id)]["sales_id"]
    return sales_person[~sales_person["sales_id"].isin(sales_ids)][["name"]]
