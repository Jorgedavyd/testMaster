from datetime import datetime
import pandas as pd
from typing import List, Tuple

class Dataset:
    path: str = '/dataset/testMaster/'

    @staticmethod
    def prepPath(variables: List[str]) -> str:
        # TODO

    @staticmethod
    def query(variables: List[str], interval: Tuple[datetime, datetime]) -> pd.DataFrame:
        df: pd.DataFrame = pd.from_json(Dataset.prepPath(variables))
        data: pd.DataFrame = df[variables]
        return data
