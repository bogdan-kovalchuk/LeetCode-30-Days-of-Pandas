import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    mask = ~customers["id"].isin(orders["customerId"])
    customers_no_orders = customers[mask][["name"]]
    return customers_no_orders.rename(columns={"name": "Customers"})
