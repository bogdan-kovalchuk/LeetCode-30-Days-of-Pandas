import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    d = teacher.groupby("teacher_id", as_index=False)["subject_id"].nunique()
    return d.rename(columns={"subject_id": "cnt"})
