import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    g = actor_director.groupby(["actor_id", "director_id"], as_index=False).size()
    return g[g["size"] >= 3][["actor_id", "director_id"]]
