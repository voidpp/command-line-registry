
import os
from configpp.tree import Tree, NodeBase
from configpp.soil import Config as ConfigLoader, Location
from typing import List


tree = Tree()


class App(NodeBase):

    name: str
    desc = ""

    def serialize(self):
        return self.__dict__


AppList = List[App]


@tree.root()
class Config():

    apps: AppList


loader = ConfigLoader('command-line-registry.json')


def load() -> Config:
    if not loader.load():
        return None
    return tree.load(loader.data)


def save(config: Config = None) -> Config:

    if config:
        loader.data = tree.dump(config)
        loader.dump()
        return config

    loader.data = {'apps': []}
    loader.dump(Location(os.path.expanduser('~')))

    return tree.load(loader.data)
