import pandas as pd
import re


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def is_valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$"
        return bool(re.fullmatch(pattern, email))

    return users[users["mail"].apply(is_valid_email)]
