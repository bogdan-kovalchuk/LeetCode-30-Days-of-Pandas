import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    all_combinations = pd.merge(students, subjects, how="cross")
    exam_counts = examinations.groupby("student_id", as_index=False)["subject_name"].value_counts()
    merged_df = pd.merge(all_combinations, exam_counts, on=["student_id", "subject_name"], how="left", sort=True)
    merged_df["count"] = merged_df["count"].fillna(0).astype(int)
    merged_df = merged_df.rename(columns={"count": "attended_exams"})
    return merged_df
