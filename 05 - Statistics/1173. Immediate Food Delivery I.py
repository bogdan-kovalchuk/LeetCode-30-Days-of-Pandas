import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = (
        delivery["order_date"] == delivery["customer_pref_delivery_date"]
    ).sum()
    total = delivery.shape[0]
    return round(immediate / total * 100, 2)
