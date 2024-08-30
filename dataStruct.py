from datetime import datetime
from dataclasses import dataclass
from typing import Any, Dict,List, Tuple
import aiofiles
import json
import pandas as pd

@dataclass
class Name:
    filepath: str

    def __post_init__(self) -> None:
        self.postProcess()

    def postProcess(self) -> None:
        if prep:=self.filepath.split('/')[-1]:
            if filename:=prep.split('-'):
                self.context: str = filename[0]
                self.date: datetime = datetime.strptime(filename[1], '%Y%m%d')
                self.branch: str = filename[2]
                if '~' in self.branch:
                    self.branch.replace('~', '-')
                self.user: str = filename[3]
                if '~' in self.user:
                    self.user.replace('~', '-')
                self.id: int = int(filename[4][:-4])
            else:
                raise ValueError("Not valid name")
        else:
            raise ValueError("Not valid path")

VALID_SUBTEST_ITEMS: List[str] = [
    'result',
    'timeCreated',
    'timeStarted',
    'timeCompleted',
]

@dataclass
class SubTest:
    def __init__(self, **kwargs) -> None:
        for item in kwargs:
            if item in VALID_SUBTEST_ITEMS:
                setattr(self, item, kwargs[item])

        self.result: bool = True if 'passed' else False
        self.timeCreated: datetime = datetime.fromtimestamp(self.timeCreated/1000)
        self.timeStarted: datetime = datetime.fromtimestamp(self.timeStarted/1000)
        self.timeCompleted: datetime = datetime.fromtimestamp(self.timeCompleted/1000)

VALID_ITEMS: List = [
    'name',
    'path',
    'result',
    'status',
    'isDataDriven',
    'timeCreated',
    'timeStarted',
    'timeCompleted',
    'actions',
    'subtests'
]

class Test:
    def __init__(self, **kwargs) -> None:
        for item in kwargs:
            if item in VALID_ITEMS:
                setattr(self, item, kwargs[item])

        if getattr(self, 'isDataDriven'):
            self.realSubtest: List[SubTest] = []
            del self.actions
            for subtest in self.subtests:
                self.realSubtest.append(Test(**subtest))

VALID_ACTION_ITEMS: List[str] = [
    'action',
    'actorType',
    'durationMs',
    'result',
]

@dataclass
class Actions:
    def __init__(self, **kwargs) -> None:
        for item in kwargs:
            if item in VALID_ACTION_ITEMS:
                setattr(self, item, kwargs[item])

        self.result = True if 'passed' else False

class Session:
    def __init__(self, json: Dict[str, Any]) -> None:
        self.tests: List[Test] = [Test(**test_params) for test_params in json['tests']]

