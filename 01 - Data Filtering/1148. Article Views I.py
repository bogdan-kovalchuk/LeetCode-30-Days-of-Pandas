import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = views["author_id"] == views["viewer_id"]
    ids = views[mask][["author_id"]].rename(columns={"author_id": "id"})
    unique = ids.drop_duplicates(subset=["id"])
    sorted = unique.sort_values(by=["id"], ascending=True)
    return sorted
