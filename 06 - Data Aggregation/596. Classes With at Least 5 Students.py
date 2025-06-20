import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses["class"].value_counts().reset_index().query("count >= 5")[["class"]]
