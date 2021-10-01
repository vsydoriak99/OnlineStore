from abc import ABC, abstractmethod

from faker import Faker


class BaseEntity(ABC):

    def __init__(self):
        pass

    def to_json(self) -> dict:
        return self.__dict__

    @staticmethod
    @abstractmethod
    def generateRandom():
        raise NotImplementedError
