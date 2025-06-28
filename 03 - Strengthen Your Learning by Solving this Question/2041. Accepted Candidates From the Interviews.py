import pandas as pd


def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    r = rounds.groupby("interview_id", as_index=False)["score"].sum()
    c = pd.merge(candidates, r, how="left")
    return c[(c["years_of_exp"] >= 3) & (c["score"] > 15)][["candidate_id"]]
