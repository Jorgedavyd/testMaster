from collections.abc import Coroutine
from typing import List
import aiofiles
import json
import pandas as pd
import aioftp

class API:
    def __init__(self, ftp: str) -> None:
        self.ftp: str = ftp

    async def download_url(self, url: str):
        async with

    async def getPaths(self, url: str) -> None:

    def getPathTasks(self) -> List[Coroutine]:
        return [getPaths()

    def get_ftp_tasks(self) -> None:
        return [download_url]

class Formatter:
    def __init__(self) -> None:
        pass

class Dataset:
    self.result = 'result'

