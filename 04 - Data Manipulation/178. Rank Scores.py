import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    s = (
        scores["score"]
        .drop_duplicates()
        .sort_values(ascending=False)
        .to_frame(name="score")
    )
    s["rank"] = range(1, len(s) + 1)
    d = pd.merge(scores, s)
    return d[["score", "rank"]].sort_values(by="rank")
