import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.rename(columns={"event_date": "first_login"})
    return activity.groupby(by=["player_id"], as_index=False)["first_login"].min()
