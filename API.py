from collections.abc import Coroutine
from typing import List
import aiofiles
import json
import pandas as pd
import aioftp

## to druid
class API:
    endpoint: str = 'http://localhost:8081/druid'
    ftp: str = 'dfinir'

    def __init__(self) -> None:

    async def download_url(self, session, url: str) -> Any:
        async with session.get(url, ssl = False) as request:
            data = await request.json()
            return data

    async def getPaths(self, url: str) -> None:

    def getPathTasks(self) -> List[Coroutine]:
        return [getPaths()

    def processFile(self) ->
    def __call__(self) -> None:
        with aiohttp.ClientSession() as session:
            await asyncio.gather(*self.getDownloadJSONTasks())
            await asyncio.gather(*slef.getDruidTasks())

    def getDruidTasks(self) -> List[Coroutine]:
        return [self.singleToDruid() for _ in ]

    def getDownloadJSONTasks(self) -> List[Coroutine]:
        return [self.download_url() for _ in ]

    def singleToDruid(self, session, data) -> None:
        async with session.post(self.endpoint, json=data) as response:
            if response.status == 200:
                response_data = await response.data()
            else:
                print('Error')
                response_test = await response.text()
                print('Error: ')

    def get_ftp_tasks(self) -> None:
        return [download_url]

